from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense, Income
from .serializers import ExpensesSerializers, IncomesSerializers

class ExpenseList(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpensesSerializers(expenses, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class IncomeList(APIView):
    def get(self, request):
        incomes = Income.objects.all()
        serializer = IncomesSerializers(incomes, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass