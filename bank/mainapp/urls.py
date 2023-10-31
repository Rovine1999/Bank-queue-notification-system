from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'branches', views.BranchViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'queues', views.QueueViewSet)

urlpatterns = [
    path('login/', views.CustomLogin.as_view()),
    path('pick-customer/', views.PickCustomerView.as_view()),
    path('finish-serving/', views.FinishServingView.as_view()),
    path('', include(router.urls)),
]
