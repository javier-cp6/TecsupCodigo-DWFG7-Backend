# conjunto (set)
# colección de datos sin orden
meses = {'enero', 'febrero', 'marzo', 'abril'}
print(meses)
print('enero' in meses)  # True
print('agosto' in meses)  # False

# add
meses.add('mayo')
meses.add('junio')
print(meses)  # {'enero', 'mayo', 'abril', 'junio', 'marzo', 'febrero'}

# update para agregar un conjunto de elementos
meses.update(['julio', 'agosto'])
# {'enero', 'mayo', 'abril', 'junio', 'julio', 'marzo', 'agosto', 'febrero'}
print(meses)

# discard o remove eliminan todos los items del valor indicado
meses.discard('junio')
print(meses)
meses.remove('julio')
print(meses)
