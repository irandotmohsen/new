from django.db.models import fields
from rest_framework import serializers
from rest_framework import employees

class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ('first_name', 'last_name')