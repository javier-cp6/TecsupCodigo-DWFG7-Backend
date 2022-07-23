from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from .models import User

class RegisterView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

  # def post(self, request: Request):
  #   body = request.data
  #   serializerInstance = self.serializer_class(data=body)

  #   validation = serializerInstance.is_valid(raise_exception=True)
  #   if validation == True:
  #     serializerInstance.save()


