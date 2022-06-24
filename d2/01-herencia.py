class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Polimorfismo es la definición del mismo método en difrentes clases pero con un comportamiento distinto

    # info no es palabra reservada. En este caso se declara que info devuelva un objeto

    def info(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
        }


class Alumno(Usuario):
    def __init__(self, Nombre, apellido, anio, seccion):
        self.anio = anio
        self.seccion = seccion

        # método super() permite utilizar los métodos y atributos de la clase padre. De esta forma, se llama al constructor del PADRE
        # Debe declararse la misma cantidad de parámetros de la clase padre
        super().__init__(nombre=Nombre, apellido=apellido)

    def info(self):
        # return {
        #     'nombre': self.nombre,
        #     'anio': self.anio,
        #     'apellido': self.apellido,
        #     'seccion': self.seccion
        # }

        infoUsuario = super().info()
        data = {
            'anio': self.anio,
            'seccion': self.seccion
        }
        # const x = {nombre: 'eduardo', dia:'jueves'}
        # const { nombre } = x
        # const y = {...x}
        # En Python se hace desestructuración con {} y spread operator con **.
        print(data)
        print({**data})  # {'anio': 'Sexto', 'seccion': 'A'}
        # concatenar diccionarios
        return {**data, **infoUsuario}


alumnoEduardo = Alumno('Eduardo', 'de Rivero', 'Sexto', 'A')
usuarioRaul = Usuario('Raul', 'Mendoza')

print(alumnoEduardo)
print(alumnoEduardo.info())
print(usuarioRaul.info())
