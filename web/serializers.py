from django.db.models import fields
from rest_framework import serializers
from .models import Employees

class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name')