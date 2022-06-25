from flask import Flask

# __name__ variable propia de python que muestra si el archivo que estamos utulizando es el principal del proyecto. Si es el principal, su valor era '__main__', caso contratio indicará otro valor
app = Flask(__name__)

# no es posible levantar 2 servidores para el mismo proyecto. Principio singleton: no es posible tener varias instancias. En este caso la instancia es Flask

# Endpoint
# decorador: patrón de software que se utiliza para modificar el comportamiento de un método (de una clase) sin la necesidad de emplear otros métodos como la herencia. Además, es necesario modificar el comportamiento del método de dicha clase
# inician con @


@app.route('/')
def rutaInicial():
    print('ingreso al endpoint inicial')
    return 'Bienvenido a tu primera API Tecsup 10'


# levantar servidor para que quede a la espera de posibles peticiones durante un tiempo indeterminado

# debug: indicará que si estamos en un servidor de prueba, cada vez que se haga algún cambio a algún archivo del proyecto automáticamente se reiniciará el servidor con los cambios. Valor por defecto es False

app.run(debug=True)
