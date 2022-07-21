from rest_framework import serializers

class TestSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=40)
  lastname = serializers.CharField(max_length=40)