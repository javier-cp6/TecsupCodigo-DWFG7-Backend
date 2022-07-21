from django.urls import path
from .views import start, TestView

urlpatterns = [ 
  path('start', start),
  path('test', TestView.as_view())
]