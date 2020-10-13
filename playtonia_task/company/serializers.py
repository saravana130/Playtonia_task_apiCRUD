from rest_framework import serializers
from .models import *

class CompanySerializer (serializers.ModelSerializer):
    class Meta:
        model=company
        fields = '__all__'


class EmployeesSerializer (serializers.ModelSerializer):
    class Meta:
        model= employees
        fields = '__all__'