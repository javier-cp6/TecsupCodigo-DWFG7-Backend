alumnos = ["Saul", "Alejandro", "Alexandra", "Jenny"]
otra = [1, 10, 'hola', True, 5.2, None]

print(alumnos[0])
# python emite un error cuando se intenta acceder a una posición que no existe. a diferencia de js que emite undefined
# print(alumnos[10])

variados = [10, [1, 2, 3]]
print(variados[1][1])

# en la [posición] de una lista se puede indicar un rango y devuelve una nueva lista
print(alumnos[1:3])  # ['Alejandro', 'Alexandra']

# posición en sentido invertido
print(alumnos[-1])  # Jenny

# sentido de pertenencia
print('Saul' in alumnos)  # True
print(10 in alumnos)  # False

# las listas son colecciones de datos EDITABLES
alumnos[0] = 'Martin'
print(alumnos)  # ['Martin', 'Alejandro', 'Alexandra', 'Jenny']

# append
alumnos.append('Ivan')
print(alumnos)  # ['Martin', 'Alejandro', 'Alexandra', 'Jenny', 'Ivan']

# extend para combinar listas. Funciona también con +
alumnos.extend(['Luis', 'Beto'])
print(alumnos)

alumnos += ['Yordy', 'Ruben']
print(alumnos)

# del para eliminar elemento de una lista
del alumnos[1:3]
print(alumnos)

# pop retira valor de lista y lo asigna a la variable
alumno_eliminado = alumnos.pop(2)
print(alumnos)
print(alumno_eliminado)

# clear deja una lista sin valores []
alumnos.clear()
print(alumnos)
