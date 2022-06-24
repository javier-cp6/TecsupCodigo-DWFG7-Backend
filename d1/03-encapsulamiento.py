# Pilares
# 1. Abstracción
# 2. Encapsulamiento
# 3. Herencia
# 4. Polimorfismo

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # atributo privado inicia con __
        self.__serie = marca+modelo
        # TODO: explicar el tipo PROTECTED
        # A diferencia de otros lenguajes, en Python es posible acceder a un atributo protegido y al momento de hacer herencia no modifica los valores (al crear el mismo atributo en las clases hijas)
        self._serie2 = marca+modelo

    # método para acceder a atributo privado
    def mostrarSerie(self):
        print(self.__serie)


auto = Vehiculo('Kia', 'Picanto')
camion = Vehiculo('Volvo', 'F30')
print(auto.marca)  # Kia
# print(auto.__serie)  # error
auto.mostrarSerie()  # KiaPicanto
print(auto._serie2)  # KiaPicanto
