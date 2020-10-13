from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = CompanySerializer

class EmployeesViweSet(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = EmployeesSerializer
