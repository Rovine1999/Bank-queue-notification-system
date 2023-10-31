from django.db import models
from django.contrib.auth.models import User

#TimeStamp model to add created_at and updated_at fields to all models
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        abstract = True

#Branch model
class Branch(TimeStampedModel):
    name = models.CharField(blank=False, null=False, max_length=100)

#model(table) for employee
class Employee(TimeStampedModel):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, blank=False, null=True, on_delete=models.SET_NULL)
    employee_no = models.CharField(max_length=50, blank=True, null=True)

#model(table) for customer
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
    state = models.CharField(default='0', choices=STATE_CHOICES, max_length=4)
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL)


class EmployeeQueueAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    serving = models.BooleanField(default=False)
