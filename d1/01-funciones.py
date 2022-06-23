# función
# bloque de código que no se ejecuta automáticamente

def saludar():
    print('Buenas tardes')


saludar()


def saludarConNombre(nombre):
    # Triple comilla para documentar una función:
    '''Funciíon que recibe un nombre y saluda'''
    print('Hola {}, ¿cómo te va?'.format(nombre))


saludarConNombre('Saul')


def calcularIGV(valor):
    """Función que recibe el valor y devuelve el valor incluido el IGV"""
    valorIncluidoIGV = valor * 1.18
    return valorIncluidoIGV


precio = 100
precioConIGV = calcularIGV(precio)
print(precioConIGV)


def calcularSalarioMinimo(profesion, experiencia):
    salarioMinimo = 1050
    if profesion == 'Desarrollador':
        if experiencia == 'Básica':
            salarioMinimo = 3000
        elif experiencia == 'Media':
            salarioMinimo = 4000
        elif experiencia == 'Avanzada':
            salarioMinimo = 7000

    elif profesion == 'Marketing':
        if experiencia == 'Básica':
            salarioMinimo = 2500
        elif experiencia == 'Media':
            salarioMinimo = 4150
        elif experiencia == 'Avanzada':
            salarioMinimo = 6850

    return salarioMinimo


profesion, experiencia = 'Desarrollador', 'Media'
salario = calcularSalarioMinimo(profesion, experiencia)
print(salario)

profesion, experiencia = 'Marketing', 'Básica'
salario = calcularSalarioMinimo(profesion, experiencia)
print(salario)

profesion, experiencia = 'Astronauta', 'Avanzada'
salario = calcularSalarioMinimo(profesion, experiencia)
print(salario)

# para indicar los parámetros en un orden distinto
salario = calcularSalarioMinimo(experiencia='Básica', profesion='Marketing')
print(salario)


electrodomesticos = []


def registrarElectrodomesticos(nombre, precio, almacen='Las Malvinas'):
    electrodomesticos.append(
        # diccionario
        {'nombre': nombre, 'precio': precio, 'almacen': almacen})
    return True


registrarElectrodomesticos('Licuadora 12 velocidades', 115.00)
registrarElectrodomesticos('Freidora de aire', 100, 'Cercado')
registrarElectrodomesticos('Secadora de cabello', 140)
registrarElectrodomesticos('Radio FM', 100, 'Arequipa')
print(electrodomesticos)  # devuelve un array de diccionarios

# acceder a un elemento de un diccionario dentro de un array
print(electrodomesticos[0]['almacen'])


def contarElectrodomesticosPorAlmacen():
    '''Cuenta cantidad de electrodomésticos en cada almacén'''
    malvinas = 0
    cercado = 0
    otro = 0
    for item in electrodomesticos:
        if item['almacen'] == 'Las Malvinas':
            malvinas += 1
        elif item['almacen'] == 'Cercado':
            cercado += 1
        else:
            otro += 1

    # print("En Las Malvinas hay {} electrodomésticos, en El Cercado hay {} electrodomésticos y en otros hay {} electrodomésticos ".format(
    #     malvinas, cercado, otro))
    return [malvinas, cercado, otro]


resultado = contarElectrodomesticosPorAlmacen()
print("En Las Malvinas hay {} electrodomésticos, en El Cercado hay {} electrodomésticos y en otros hay {} electrodomésticos ".format(
    resultado[0], resultado[1], resultado[2]))

# para recibir un número indeterminado de argumentos, declarar el parámtro con *


def recibirAlumnos(clase, *alumnos):
    print(type(alumnos))  # <class 'tuple'>
    print(alumnos)  # ('Juan Carlos', 'Manuel', 'Wilson', 'Alejandro')
    lista = list(alumnos)  # <class 'list'>
    print(type(lista))  # <class 'list'>
    lista[0] = 'Rigoberto'
    print(lista)  # ['Rigoberto', 'Manuel', 'Wilson', 'Alejandro']
    print(clase)  # Eduardo


recibirAlumnos('Eduardo', 'Juan Carlos', 'Manuel')
# devuelve una tupla ('Eduardo', 'Juan Carlos', 'Manuel', 'Wilson', 'Alejandro')
recibirAlumnos('Eduardo', 'Juan Carlos', 'Manuel', 'Wilson', 'Alejandro')
