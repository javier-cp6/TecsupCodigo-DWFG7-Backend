from django.urls import path
# vista que brinda tokens de acceso y fresh
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login', TokenObtainPairView.as_view())
]
