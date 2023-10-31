from django.contrib import admin
from .models import Branch, Employee, Customer, Queue, EmployeeQueueAssignment


admin.site.register([Branch, Employee, Customer, Queue, EmployeeQueueAssignment])
