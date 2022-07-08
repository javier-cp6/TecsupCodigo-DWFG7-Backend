from flask import Flask
from config import conexion
from models.participante import Participante

from dotenv import load_dotenv
# environ devuelve las variables de entorno como un diccionario
from os import environ
app = Flask(__name__)

# cargar las variables de .env como si fuesen variables de entorno  para que puedan ser accedidas por environ
load_dotenv()

# en todos los moteres
# URI dialect://usuario:password@host:puerto/base_de_datos
# en mysql el puerto siempre es 3306
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:password:root@localhost:3306/concierto'
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']

# sqlalchemy hace un seguimiento a las modificaciones que se hagan en la db (por defecto). En futuras versiones se tendrá que indicar obligatoriamente y no será por defecto.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# inicializa conexión de sqlalchemy con la db, pero aún no se conecta (setea valoresde conexión)
conexion.init_app(app)

# se ejecuta la conexión y se crean las tablas.
# Si no hay ninguna tabla a crear, no lanzará error de credenciales inválidas
conexion.create_all(app=app)
if __name__ == '__main__':
    app.run(debug=True)
