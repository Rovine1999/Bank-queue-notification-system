from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, Employee


@receiver(post_save, sender=Customer)
def new_customer_creation_signal(sender, instance, created, **kwargs):

    if created:
        customer_group = Group.objects.filter(name="customer").first()
        if customer_group:
            instance.user.groups.add(customer_group)
            instance.user.save()


@receiver(post_save, sender=Employee)
def new_employee_creation_signal(sender, instance, created, **kwargs):

    if created:
        customer_group = Group.objects.filter(name="employee").first()
        if customer_group:
            instance.user.groups.add(customer_group)
            instance.user.save()

