from django.urls import path
from rest_framework import routers
from .views import CompanyViewSet,EmployeesViweSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeesViweSet)
router.register(r'company', CompanyViewSet)


