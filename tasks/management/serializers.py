from dataclasses import field, fields
from rest_framework import serializers
from .models import Task

class TestSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=40)
  lastname = serializers.CharField(max_length=40)

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'