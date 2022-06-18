numeros = [10, 20, 30, 40, 50, 60]

for numero in numeros:
    print(numero)

# contador o flag
frase = 'Al que madruga, encuentra todo cerrado'
# cuántas letras "n" hay en la frase?

contador = 0
for caracter in frase:
    if caracter == 'n':
        contador += 1
print("La letra 'n' se encuentra {} veces en la frase".format(contador))  # 2

# for in range(start, end+1, step)
for valor in range(10):
    print(valor)  # 0...9

for valor in range(5, 9):
    print(valor)  # 5... 8

for valor in range(4, 10, 2):
    print(valor)  # 4, 6, 8

numeros = [10, 30, 12, 17, 24, 67]
contador_pares = 0
contador_multiplos_tres = 0
for item in numeros:
    if item % 2 == 0:
        contador_pares += 1
    if item % 3 == 0:
        contador_multiplos_tres += 1
print("La lista tiene {} números pares y {} multiplos de tres".format(
    contador_pares, contador_multiplos_tres))

# break
for valor in range(0, 10000):
    print(valor)
    if(valor == 600):
        print('El valor fue encontrado')
        break

# continue
for valor in range(0, 20):
    if(valor == 5):
        print("Usuario encontrado")
        continue
    # debido al continue previo, esta línea se ejecuta mientras NO se cumpla el if
    print(valor)

# pass
for valor in range(0, 20):
    # TODO # implementar la lógica
    pass

# for else
alumnos = ["Eduardo", "Lily", "Jose", "Rafael"]
for alumno in alumnos:
    if alumno == "Luis":
        print('Bienvenido {}'.format(alumno))

else:  # se ejecuta cuando termina la iteración previa
    print("No se encontró el alumno")
