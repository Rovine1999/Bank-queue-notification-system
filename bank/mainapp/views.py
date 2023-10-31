from django.utils import timezone
from rest_framework import viewsets, filters, permissions
from .models import Branch, Employee, Customer, Queue, EmployeeQueueAssignment
from .serializers import UserSerializer, EmployeeSerializer, BranchSerializer, CustomerSerializer, QueueSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .auth import AUTH_CLASS
from .permissions import IsAuthenticatedOrPostOnly
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView

from .utils import send_notification


class CustomLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user': UserSerializer(user).data
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [IsAuthenticatedOrPostOnly]
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = BranchSerializer
    filter_backends = [filters.OrderingFilter]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [IsAuthenticatedOrPostOnly]
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [IsAuthenticatedOrPostOnly]
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    filterset_fields = []


class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = QueueSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    filterset_fields = []


class PickCustomerView(APIView):
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [AUTH_CLASS]

    def get_queryset(self):
        branch_id = self.request.data.get('branch')
        return Queue.objects.filter(branch_id=branch_id, state='0')

    def post(self, request):
        branch_id = request.data.get('branch')
        employee_id = request.user.employee.id
        employee_name = request.user.get_full_name()

        active_queues = Queue.objects.filter(branch_id=branch_id, state='0')
        last_served = EmployeeQueueAssignment.objects.filter(
            employee_id=employee_id, serving=True
        ).order_by('-start_time').first()

        if last_served:
            last_served.serving = False
            last_served.end_time = timezone.now()
            last_served.save()

        next_queue = active_queues.exclude(
            Q(employeequeueassignment__employee_id=employee_id, employeequeueassignment__serving=True)
        ).order_by('created_at').first()

        if next_queue:
            assignment = EmployeeQueueAssignment.objects.create(
                employee_id=employee_id,
                queue=next_queue,
                start_time=timezone.now(),
                serving=True
            )
            assignment.serving = True
            assignment.save()
            next_queue.state = '1'
            next_queue.save()
            # Send email notification (This can be changed to send an sms notification)
            customer_email = next_queue.customer.user.email
            message = f"Hello {customer_email}, you are next in the service. Visit teller No. {employee_id} ({employee_name})"
            send_notification(customer_email, message)

            return Response({'message': f"Queue {next_queue.id} assigned to Employee {employee_id}"})
        else:
            return Response({'message': 'No queues available'})


class FinishServingView(APIView):
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [AUTH_CLASS]

    def get_queryset(self):
        employee_id = self.request.user.employee.id
        return EmployeeQueueAssignment.objects.filter(employee__id=employee_id, serving=True)

    def post(self, request):
        active_assignment = self.get_queryset().first()
        employee_id = request.user.employee.id
        employee_name = request.user.get_full_name()

        if active_assignment:
            active_assignment.serving = False
            active_assignment.end_time = timezone.now()
            active_assignment.save()

            active_queue = active_assignment.queue
            active_queue.state = '2'
            active_queue.save()

            customer_email = active_queue.customer.user.email
            message = (f"Hello {customer_email}, we believe you have been served well. Kindly leave a review for the "
                       f"branch."
                       f"({employee_name})")
            send_notification(customer_email, message)

            return Response({'message': f"Queue {active_queue.id} is closed for Employee {active_assignment.employee_id}"})
        else:
            return Response({'message': 'No active queue being served by the employee'})

