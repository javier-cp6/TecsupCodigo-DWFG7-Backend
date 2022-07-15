from django.db import models

# Create your models here.


class Tarea(models.Model):
    # tipos de datos

    # opciones de las columnas
    estadoOpciones = [('POR_HACER', 'POR HACER'),
                      ('HACIENDO', 'HACIENDO'), ('HECHO', 'HECHO')]

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    fechaVencimiento = models.DateTimeField(
        db_column='fecha_vencimiento')
    estado = models.CharField(choices=estadoOpciones,
                              max_length=10, default='POR_HACER')


class Meta:
    db_table = 'tareas'
    # ordenamiento descendente por la fecha de vencimiento
    ordering = ['-fechaVencimiento']
