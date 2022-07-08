from config import conexion
from sqlalchemy import Column, types


class Participante(conexion.Model):
    # esta clase tendra un comportamiento en forma de una tabla en la db. todos los atributos declarados que sean propios de la db se crearán como columnas
    # crear una columna con el nombre id en la tabla Participante

    # conexion.Column() === Column(), es lo mismo
    # https://docs.sqlalchemy.org/en/14/core/metadata.html?highlight=column#sqlalchemy.schema.Column.__init__

    # si no se indica el parámetro 'name', se considera el mismo que el nombre del atributo (p. ej. id)
    # id = Column(name = 'id')

    # cuando se usa un tipo de dato en mayúsculas sólo será para un determinado motor de db. se recomienda utilizar los nombres genéricos. Por ejemplo, en PostgreSQL es necesario porque utiliza tipo de datos espaciales

    # id INT PRIMARY KEY AUTO_INCREMENT
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    # nombre VARCHAR(50) NOT NULL
    nombre = Column(type_=types.String(50), nullable=False)
    apellido = Column(type_=types.String(50), nullable=False)
    telefono = Column(type_=types.String(10))
    password = Column(type_=types.Text, nullable=False)
    zona = Column(type_=types.Enum('SUPER VIP', 'VIP', 'GENERAL'),
                  default='GENERAL', nullable=False)
    comentario = Column(type_=types.Text)
    correo = Column(type_=types.String(45), nullable=False)

    # modificación de nombre de tabla a nivel de db para que no se llame igual que la clase (singular y la primera letra en mayúscula)
    __tablename__ = 'participantes'
