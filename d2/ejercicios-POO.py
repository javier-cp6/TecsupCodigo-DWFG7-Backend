# Crear una clase Persona en la cual se guarde el nombre, fecha_nacimiento, nacionalidad y dni.  Además, crear las clases Alumno y Docente. La primera, tendrá una serie de cursos matriculados, mientras que la segunda tendrá el número del seguro social y cuenta de CTS. En base al concepto de herencia, crear las clases indicadas y evaluar si algún atributo o método debe ser privado.

class Persona:
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni):
        self.nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.__dni = dni

    def info(self):
        return {
            'nombre': self.nombre,
            'fecha_nacimiento': self.__fecha_nacimiento,
            'nacionalidad': self.nacionalidad,
            'dni': self.__dni
        }

    def mostrarFechaNacimiento(self):
        return self.__fecha_nacimiento

    def mostrarDNI(self):
        return self.__dni


class Alumno(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni, cursos_matriculados):
        self.cursos_matriculados = cursos_matriculados

        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)

    def info(self):
        # infoAlumno = super().info()
        # data = {
        #     'cursos_matriculados': self.cursos_matriculados
        # }
        # return {**infoAlumno, **data}

        return {
            'nombre': self.nombre,
            'fecha_nacimiento': super().mostrarFechaNacimiento(),
            'nacionalidad': self.nacionalidad,
            'dni': super().mostrarDNI(),
            'cursos_matriculados': self.cursos_matriculados
        }


class Docente(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni, num_seguro_social, num_cta_cts):
        self.__num_seguro_social = num_seguro_social
        self.__num_cta_cts = num_cta_cts

        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)

    def mostrarNumSeguroSocial(self):
        return self.__num_seguro_social

    def mostrarNumCTS(self):
        return self.__num_cta_cts

    def info(self):
        return {
            'nombre': self.nombre,
            'fecha_nacimiento': super().mostrarFechaNacimiento(),
            'nacionalidad': self.nacionalidad,
            'dni': super().mostrarDNI(),
            'num_seguro_social': self.__num_seguro_social,
            'num_cta_cts': self.__num_cta_cts
        }


alumnoWaltDisney = Alumno('Walt Disney', '1950-01-01',
                          'Estados Unidos', '10101010', ['frontend', 'backend'])

print(alumnoWaltDisney.info())

docenteMickeyMouse = Docente('Mickey Mouse', '1970-01-01',
                             'Estados Unidos', '20202020', 'ss-19700101', 'cts-789654123')
print(docenteMickeyMouse.info())
