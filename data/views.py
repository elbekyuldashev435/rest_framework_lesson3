from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Employees
from .serializers import EmployeeSerializer
# Create your views here.


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    lookup_field = 'id'