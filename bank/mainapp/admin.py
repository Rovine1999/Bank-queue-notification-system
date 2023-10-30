from django.contrib import admin
from .models import Branch, Employee, Customer, Queue, Transaction, Notification


admin.site.register([Branch, Employee, Customer, Queue, Transaction, Notification])
