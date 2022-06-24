from unittest import result
from camelcase import CamelCase

camelcase = CamelCase()

parrafo = 'hola amigos veamos si la libreria funciona'

resultado = camelcase.hump(parrafo)
print(resultado)  # Hola Amigos Veamos Si La Libreria Funciona

# Patrón de Diseño Singleton
