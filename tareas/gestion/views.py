from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView

from .serializers import PruebaSerializer, TareaSerializer
from .models import Tarea
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request):
    # request da toda la información del cliente que hace la petición
    print(request)
    return Response(data={
        'message': 'Endpoint de un decorador',
    })


class PruebaView(ListAPIView):
    # en cualquiera de las clases genéricas se necesita declarar los atributos
    queryset = [{
        'nombre': 'eduardo',
        'apellido': 'de rivero'
    }, {
        'nombre': 'roxana',
        'apellido': 'gonzales'
    }]
    # serializador es un DTO (Data Transfer Object)
    serializer_class = PruebaSerializer

# ListCreateAPIView admite GET y POST
class TareasView(ListCreateAPIView):
    queryset = Tarea.objects.all() # SELECT * FROM tareas
    serializer_class = TareaSerializer

    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     return Response(data = {
    #         'message': "Aún no hay tareas"
    #     })
    def get(self, request):
        # cuando se modifica el méteodo por algún comportamiento distinto, entonces DRF (django restful framework) obedecerá a este nuevo comportamiento. Por lo tanto, se puede dejar de utilizar queryset y serializer_class
        # primero traer las tareas
        #  

        usuarioId = request.user.id
        # tareas = self.get_queryset()
        tareas = Tarea.objects.filter(usuarioId = usuarioId).all()

        tareasSerializada = self.serializer_class(tareas, many = True)

        return Response(data = {
            'message': "Las tareas son",
            'content': tareasSerializada.data
        },status=status.HTTP_200_OK)

    def post(self, request: Request):
        body = request.data # body
        
        print(request.user.nombre)
        body['usuarioId'] = request.user.id

        
        instanciaSerializador = self.serializer_class(data = body)
        validacion = instanciaSerializador.is_valid(raise_exception=True) # retorna true si es válida, sino emite error 
        if validacion == True:
            # save guarda la información en la db
            instanciaSerializador.save()

            return Response(data = instanciaSerializador.data, status=status.HTTP_201_CREATED)
