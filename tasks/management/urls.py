from django.urls import path
from .views import start, TestView, TaskView

urlpatterns = [ 
  path('start', start),
  path('test', TestView.as_view()),
  path('task', TaskView.as_view())
]