from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        abstract = True


class Branch(TimeStampedModel):
    name = models.CharField(blank=False, null=False, max_length=100)


class Employee(TimeStampedModel):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, blank=False, null=True, on_delete=models.SET_NULL)
    employee_no = models.CharField(max_length=50, blank=True, null=True)


class Customer(TimeStampedModel):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, blank=False, null=True, on_delete=models.SET_NULL)


class Queue(TimeStampedModel):
    STATE_CHOICES = (
        ('0', 'NEW'),
        ('1', 'IN_SERVICE'),
        ('2', 'DONE'),
    )
    customer = models.ForeignKey(Customer, blank=False, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branch, blank=False, null=True, on_delete=models.SET_NULL)
    state = models.CharField(default='new', choices=STATE_CHOICES, max_length=4)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL)

class Transaction(TimeStampedModel):
    queue = models.ForeignKey(Queue, blank=False, null=False, on_delete=models.CASCADE)
    

class Notification(TimeStampedModel):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
