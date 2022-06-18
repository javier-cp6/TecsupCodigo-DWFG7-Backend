# las tuplas NO son editables. Se pueden utilizar para variables privadas

profesores = ('Eduardo', 'Osmar')
print(profesores[0])  # Eduardo

# profesores[0] = 'Ximena'  # error
# print(profesores)

# profesores.append('Raul') # error
# print(profesores)

data = (1, True, 'Junio', 14.5, [1, 2, 3, 4])
print(data[1:4])  # (True, 'Junio', 14.5)

# se puede elimnar toda la variable pero no el contenido de la tupla
del data

notas = (10, 15, 15, 18, 10, 5, 7, 14)

# count para contar elementos
print(notas.count(10))  # 2
print(notas.count(20))  # 0

# index retorna índice. Si no existe el valor, devuelve error
print(notas.index(15))  # 1

# TODO: cómo se podría mostrar todas las posiciones que contengan el valor 15
