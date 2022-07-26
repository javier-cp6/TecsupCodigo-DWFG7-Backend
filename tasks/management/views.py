from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
  permission_classes = [IsAuthenticated]

  def get(self, request):
    # tasks = self.get_queryset()
    userId = request.user.id
    tasks = Task.objects.filter(userId = userId).all()
    serializedTasks = self.serializer_class(tasks, many=True)

    return Response(data={
      'message': 'Task List',
      'content': serializedTasks.data
    # },status=200)
    },status=status.HTTP_200_OK)
  
  def post(self, request: Request):
    body = request.data
    print(request)
    print(request.user)
    print(request.user.name)
    body['userId'] = request.user.id
    serializerInstance = self.serializer_class(data=body)
    
    validation = serializerInstance.is_valid(raise_exception=True)
    if validation == True:
      serializerInstance.save()
      
      return Response(data=serializerInstance.data, status=status.HTTP_201_CREATED)