# Programación orientada a objetos (PPO) | OOP
# Clase: plantilla para empezar a definir atributos y métodos de un determinado objeto

from xml.dom import NoModificationAllowedErr


class Persona:
    # atributos
    estatura = 100
    colorOjos = 'Café'
    colorCabello = 'Negro'
    fechaNacimiento = '200-01-01'

    def saludar(self):
        print('Hola, buenos días')

# instanciar: crear una referencia de una clase, es decir, crear una copia de la plantilla


personaEduardo = Persona()
print(personaEduardo.colorCabello)

personaMaria = Persona()
personaMaria.colorOjos = 'Verde'
print(personaMaria.colorOjos)
print(personaMaria.colorCabello)

personaEduardo.saludar()
personaMaria.saludar()


# Constructor
# self: es la referencia de la instancia que que se ha creado en relación a su posición de memoria. De esta manera, sólo se modificarán los atributos de esta misma instancia
# obligatoriamente, self debe ser declarado como primer parámetro de TODO método de una  clase
class Mascota:
    def __init__(self, nomobre, especie, raza, sexo):
        self.nombre = nomobre
        self.especie = especie
        self.raza = raza
        self.sexo = sexo

    def info(self):
        print(self.nombre)
        print(self.especie)
        print(self.raza)
        print(self.sexo)


mascotaPerro = Mascota('Morocha', 'Perro', 'Salchicha', 'Femenino')
mascotaGato = Mascota('Michi', 'Gato', 'Siamés', 'Masculino')
print(mascotaPerro.nombre)
print(mascotaGato.nombre)
mascotaPerro.info()
