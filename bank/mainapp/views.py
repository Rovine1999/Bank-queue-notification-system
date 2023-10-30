from rest_framework import viewsets, filters, permissions
from .models import Branch, Employee, Customer, Queue, Transaction, Notification
from .serializers import UserSerializer, EmployeeSerializer, BranchSerializer, CustomerSerializer, QueueSerializer, TransactionSerializer, NotificationSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .auth import AUTH_CLASS
from .permissions import IsAuthenticatedOrPostOnly


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


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    filterset_fields = []


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all().order_by('id')
    authentication_classes = [AUTH_CLASS]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = NotificationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = '__all__'
    filterset_fields = []


