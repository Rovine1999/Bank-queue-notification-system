from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, Employee

# Signal to create a new customer
@receiver(post_save, sender=Customer)
def new_customer_creation_signal(sender, instance, created, **kwargs):

# If a new customer is created, add them to the customer group
    if created:
        customer_group = Group.objects.filter(name="customer").first()
        if customer_group:
            instance.user.groups.add(customer_group)
            instance.user.save()

# Signal to create a new employee
@receiver(post_save, sender=Employee)
def new_employee_creation_signal(sender, instance, created, **kwargs):

# If a new employee is created, add them to the employee group
    if created:
        customer_group = Group.objects.filter(name="employee").first()
        if customer_group:
            instance.user.groups.add(customer_group)
            instance.user.save()

