from django.contrib.auth.models import User
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Branch, Employee, Customer, Queue
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        init_data = self.initial_data
        _password = init_data.get('password', init_data.get('username'))
        validated_data['password'] = make_password(_password)
        return super().create(validated_data=validated_data)


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class EmployeeSerializer(WritableNestedModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Employee
        fields = '__all__'


class CustomerSerializer(WritableNestedModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Customer
        fields = '__all__'


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = '__all__'
