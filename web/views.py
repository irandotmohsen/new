from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employees
from .serializers import employeesSerializers

class emplyeeList(APIView):
    def get(self, request):
        employees1 = Employees.objects.all()
        serializer = employeesSerializers(employees1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass