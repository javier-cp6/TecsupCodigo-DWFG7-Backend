edad_saul = 50

if edad_saul >= 18:
    # debe ir una tabulación o más
    print('Se permite el acceso')
else:
    print('No se permite el acceso')

edad_martin = 70

if edad_martin >= 65:
    print('Jubilado')
elif edad_martin >= 18:
    print('Mayor de edad')
elif edad_martin > 0:
    print('Menor de edad')
else:
    print('Edad imposible')

# Input
nombre = input("Hola, ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
print(nombre, edad, "años")

talla = input("Hola, ingresa tu talla: ")

if talla.lower() == "xl":
    print('El producto llega a fin de mes')
elif talla.lower() == "m" or talla.lower() == "l":
    color = input("Ingrese color de polo: ")
elif talla.lower() == "s":
    print('Sólo se cuenta con el producto en color morado')
else:
    print('Talla incorrecta')
