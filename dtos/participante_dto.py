from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.participante import Participante


class ParticipanteResponseDTO(SQLAlchemyAutoSchema):
    # la clase meta sirve como el super()
    #  para heredar los atributos de la clase padre
    class Meta:
        # el atributo model sirve para indicar el modelo a utilizar para hacer todo lo relacionado con la serialización y deserialización
        model = Participante


class ParticipanteRequestDTO(SQLAlchemyAutoSchema):
    class Meta:
        model = Participante
