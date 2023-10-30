from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'branches', views.BranchViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'queues', views.QueueViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'notifications', views.NotificationViewSet)

urlpatterns = [
    path('login/', views.CustomLogin.as_view()),
    path('', include(router.urls)),
]