from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .serializers import RegisterSerializer
from .models import User

class RegisterView(CreateAPIView):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

  #optional
  # def post(self, request: Response):
  #   body = request.data
  #   serializerInstance = self.serializer_class(data=body)
  #   if serializerInstance.is_valid():
  #     serializerInstance.save()
  #     return Response(data={
  #       "message":"Account created successfully",
  #     }, status=status.HTTP_201_CREATED)
  #   return Response(serializerInstance.errors, status=status.HTTP_400_BAD_REQUEST)

