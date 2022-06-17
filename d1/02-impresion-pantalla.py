curso = 'Backend'
print(curso)
dia = 16

print("El curso es "+curso)
print("El curso es", curso)

# concatenar variables de disntinto tipo
# no se puede concatenar con "+"
print("El curso es "+curso+"y el día es ", dia)
print("El curso es {} y el día es {}".format(curso, dia))
print("El curso es {1} y el día es {0}".format(curso, dia))
# format siempre imprime un string
print("El curso es %s y el día es %d" % (curso, dia))
