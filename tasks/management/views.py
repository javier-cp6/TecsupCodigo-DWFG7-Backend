from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import TestSerializer, TaskSerializer
from .models import Task

@api_view(http_method_names=['GET', 'POST'])
def start(request: Request):
  print(request)
  print(request.data) 
  return Response(data={
    'message': 'Decorator endpoint'
  })

class TestView(ListAPIView):
  queryset = [{
    'name': 'guido',
    'lastname': 'van rossum'
  },{
    'name': 'brendan',
    'lastname': 'eich'
  }]
  serializer_class = TestSerializer

class TaskView(ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer