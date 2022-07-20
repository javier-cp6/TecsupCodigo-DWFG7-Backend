from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

@api_view(http_method_names=['GET', 'POST'])
def start(request: Request):
  print(request)
  print(request.data) 
  return Response(data={
    'message': 'Decorator endpoint'
  })