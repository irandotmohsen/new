from django.db.models import fields
from rest_framework import serializers
from .models import Expense, Income

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('text', 'date', 'amount')

class IncomesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('text', 'date', 'amount')