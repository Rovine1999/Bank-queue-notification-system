from django.contrib import admin
from .models import Branch, Employee, Customer, Queue, EmployeeQueueAssignment

#registering models to admin site of django to manage them from admin panel
admin.site.register([Branch, Employee, Customer, Queue, EmployeeQueueAssignment])
