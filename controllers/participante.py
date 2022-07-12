from flask_restful import Resource, request

from config import conexion
from models.participante import Participante
from dtos.participante_dto import ParticipanteRequestDTO, ParticipanteResponseDTO

# los tipos de datos que se pueden retornar son String, Int, Boolean, Arreglos y Listas, Diccionarios


class ParticipanteController(Resource):
    # esta clase se comportará como un controlador, es decir, que si definimos un método llamado get
    def get(self):
        # resultado = conexion.session.query(Participante)

        # con .all() se convierte en SELECT * FROM participantes
        # https://docs.sqlalchemy.org/en/14/orm/query.html
        resultado = conexion.session.query(Participante).all()

        # many = True indica que se está pasando una lista de instancias por lo que el DRO va a tener que iterar la lista y transformarlas en un diccionario.
        # es muy importante declarar el many = True. Si no se indica many = True asume que es una instancias en vez de una lista, y no va a iterar

        participantesSerializados = ParticipanteResponseDTO().dump(resultado, many=True)

        # retornará una lista de instancias de la clase del modelo. se pude accer a cada una de ellas a través de sus atributos y modelos (si hubiesen)
        print(resultado[0].zona)

        participantes = []

        for participante in resultado:
            participantes.append({
                'id': participante.id,
                'nombre': participante.nombre
                # ...
            })

        # retorna una lista de instancias de la clase del modelo
        # print(resultado)
        return {
            'message': 'Ingreso al get',
            'content': 'participantes',
            'content2': participantesSerializados

        }

    def post(self):
        # cuando se retorna una tupla, la primera posición será el body y la segunda el estado de la respuesta

        print(request.get_json())
        data = request.get_json()

        # forma 1
        # data_serializada = ParticipanteRequestDTO().load(data)
        # print(data_serializada)
        # return {
        #     'message': 'Ingreso al post'
        # }
        # forma 2 try except
        try:
            data_serializada = ParticipanteRequestDTO().load(data)
            print(data_serializada)

            # **data_serializada convierte ese diccionario en parámetros
            # {'nombre': 'fabio'} nombre = 'fabio'
            nuevoParticipante = Participante(**data_serializada)
            # empezar una nueva transacción
            conexion.session.add(nuevoParticipante)
            # una vez que se quiera guardar de manera permanente los cambios (insercción, actualización o elimnación) de los registros, se hace un commit
            conexion.session.commit()

            return {
                # 'message': 'Ingreso al post'
                'message': 'Participante agregado exitosamente'
            }
        except Exception as e:
            # se ejecuta en caso de que falle (emitirá una exception)
            # para deshacer los cambios de la transacción se hace uso de rollback
            conexion.session.rollback()
            return {
                'message': 'Error al ingresa el participante',
                'content': e.args
            }
