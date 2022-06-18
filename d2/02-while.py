# while
numero = 10
while numero > 0:
    print('Numero posotivo')
    print(numero)
    numero -= 1

# do while no exite en python

# solicitar 5 dígitos para la lotería que no sea mayor a 100 ni negativo
contador = 1
while contador < 6:
    numero = int(input('Ingrese número para la lotería: '))
    if numero > 0 and numero < 100:
        contador += 1
        # print(numero)
    else:
        print("Número no valido")
