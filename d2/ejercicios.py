# EJERCICIO 1
# ejemplo
# Para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea
# for numero in range(5):
#    print(numero, end="")


# EJERCICIO 2
# Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****

# solución
# ancho = int(input('Ingrese el ancho del rectángulo: '))
# altura = int(input('Ingrese la altura del rectángulo: '))
# for item in range(altura):
#     print('*' * ancho)


# EJERCICIO 3
# Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****

# solución
# longitud = int(input('Ingrese la longitud del lado del octágono: '))

# ancho = longitud
# espaciado = (longitud - 1) * 2
# for item in range(longitud - 1):
#     print(' ' * espaciado + '* ' * ancho)
#     ancho += 2
#     espaciado -= 2
# for item in range(longitud):
#     print('* ' * ancho)
# for item in range(longitud - 1):
#     ancho -= 2
#     espaciado += 2
#     print(' ' * espaciado + '* ' * ancho)


# EJERCICIO 4
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *

# solución
# altura = int(input('Ingrese la altura del triángulo: '))

# ancho = altura
# for item in range(altura):
#     print('*' * ancho)
#     ancho -= 1


# EJERCICIO 5
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

# solución
# print(100/10)
# numero = int(input('Ingrese un número entero: '))
# print(numero, end=" ")
# while numero > 1:
#     if numero % 2 == 0:
#         numero //= 2
#         print(numero, end=" ")
#         continue
#     numero = (numero * 3) + 1
#     print(numero, end=" ")


# EJERCICIO 6
# si el texto de ingreso es:
# texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
# resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]
# Hacer el codigo para ello

# solución
# texto = input("Ingrese un texto: ")
# resultado_final = []
# palabra = ''
# for item in (texto + ' '):
#     if not item == ' ':
#         palabra += item
#         continue
#     resultado_final.append(palabra.capitalize())
#     palabra = ''
# print(resultado_final)

# EJERCICIO 7
# ingresar numeros hasta que ese numero sea adivinado
numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'

# solución
# numero_input = None

# while numero_input != numero_adivinar:
#     numero_input = int(input('Ingrese un número: '))
#     if numero_input > numero_adivinar:
#         print("El número es menor que {}".format(numero_input))
#     elif numero_input < numero_adivinar:
#         print("El número es mayor que {}".format(numero_input))

# print('Acertaste!')

# EJERCICIO 8
# dado los siguientes numeros:
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1

# solución
multiplos_3 = 0
multiplos_5 = 0

for item in numeros:
    if item % 3 == 0 and item % 5 != 0:
        multiplos_3 += 1
    if item % 5 == 0 and item % 3 != 0:
        multiplos_5 += 1
print(multiplos_3, multiplos_5)
