from dataclasses import field
from rest_framework import serializers
from .models import Tarea

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length= 40)
    apellido = serializers.CharField(max_length=40)

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        # fields sierva para indicar qué atributos se van a requerir / mostrar al cliente
        # se puede declarar una lista de atributos o todos con '__all__' 
        fields = '__all__'