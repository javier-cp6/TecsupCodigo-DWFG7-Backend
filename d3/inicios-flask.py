from flask import Flask, request
from datetime import datetime
from flask_cors import CORS

# print(request) # aquí no se puede usar request

# __name__ variable propia de python que muestra si el archivo que estamos utulizando es el principal del proyecto. Si es el principal, su valor era '__main__', caso contratio indicará otro valor
app = Flask(__name__)

# la clase CORS si solamente le pasamos la instancia de nuestra clase FLASK modificará los CORS para que puedan ser accedidos por todo el mundo (cualquier origen, método o cabecera)
# CORS(app=app)
CORS(app)

productos = []

# no es posible levantar 2 servidores para el mismo proyecto. Principio singleton: no es posible tener varias instancias. En este caso la instancia es Flask

# Endpoint
# decorador: patrón de software que se utiliza para modificar el comportamiento de un método (de una clase) sin la necesidad de emplear otros métodos como la herencia. Además, es necesario modificar el comportamiento del método de dicha clase
# inician con @

# las turas deben empezar siempre con /


@app.route('/')
def rutaInicial():
    print('ingreso al endpoint inicial')
    return 'Bienvenido a tu primera API Tecsup 10'


@app.route('/estado')
def estadoAPI():
    # return un diccionario
    return {
        # python viene con algunas librerías (p. ej. datetime)
        # 'hora': datetime.now()
        'hora': datetime.now().strftime('%Y-%m-%d %H:%M%S')
    }


@app.route('/producto', methods=['POST'])
def gestionProductos():
    # print(request)
    # get_json() convierte el json que el cliente envía a un diccionario para que pueda ser interpretado por python
    print(request.get_json())
    producto = request.get_json()
    productos.append(producto)
    return {
        'message': 'Producto creado exitosamente',
        'content': producto
    }


@app.route('/devolver-productos', methods=['GET'])
def devolverProductos():
    return {
        'message': 'Los productos son: ',
        'content': productos
    }


# levantar servidor para que quede a la espera de posibles peticiones durante un tiempo indeterminado
# debug: indicará que si estamos en un servidor de prueba, cada vez que se haga algún cambio a algún archivo del proyecto automáticamente se reiniciará el servidor con los cambios. Valor por defecto es False
app.run(debug=True)
