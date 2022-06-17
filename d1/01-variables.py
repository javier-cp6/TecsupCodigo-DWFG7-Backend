# Python es sensible a las tabulaciones, las cuales generan errores de identación

nombre = "javier"
edad = 29
# con . se accede directamente a los métodos
nombreConMayuscula = nombre.capitalize()
print(nombreConMayuscula)

saludo = 'aloh\'a a todos'
saludo2 = "aloh'a a todos"

# en python no está permitido el uso de backticks ``
print(saludo)
print(saludo2)

# triple "  o ' permite insertar saltos de línea
despedida = """hola
a todos"""
print(despedida)

fecha = None  # similar a undefined en js

mascota, edad = "daddy", 5
print(mascota, edad)

print(type(mascota))

# se recomienda usar el mismo formato de fecha YYYY-MM-DD HH:MM:SS:zzzz