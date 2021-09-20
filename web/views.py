from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import employeesSerializers

class emplyeeList(APIView):
    def get(self, request):
        employees1 = Employees.objects.all()
        serializer = employeesSerializers(employees1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass