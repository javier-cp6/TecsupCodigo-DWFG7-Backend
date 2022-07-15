from django.urls import path
from .views import inicio, PruebaView

# serán todas las rutas que pueden ser accedidas a esta aplicación
# debe llamarse 'urlpatterns'
urlpatterns = [
    path('inicio', inicio),
    path('prueba', PruebaView.as_view())
]
