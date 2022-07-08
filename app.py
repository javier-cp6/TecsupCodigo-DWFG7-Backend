from flask import Flask
from config import conexion
app = Flask(__name__)

# inicializa conexión de sqlalchemy con la db, pero aún no se conecta (setea valoresde conexión)
conexion.init_app(app)

# se ejecuta la conexión y se crean las tablas.
# Si no hay ninguna tabla a crear, no lanzará error de credenciales inválidas
conexion.create_all(app=app)
if __name__ == '__main__':
    app.run(debug=True)
