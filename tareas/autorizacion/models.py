from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class ManejoUsuario(BaseUserManager):
  # clase que sirve para manejar el comportamiento al crear el usuario
  def create_user(self, correo, nombre, apellido, password):
    if not correo:
      raise ValueError('El usuario debe tener obligatoriamente un correo')
    # normalizar el correo, es decir, eliminar algún caracter especial y espacios
    correo = self.normalize_email(correo)
    # crear nuevo usuario
    nuevoUsuario = self.model(correo=correo, nombre=nombre, apellido=apellido)
    # hashear la contraseña
    nuevoUsuario.set_password(password)

    nuevoUsuario.save()
    return nuevoUsuario

  def create_superuser(self, correo, nombre, apellido, password):
    # creación de super usuario por consola
    nuevoUsuario = self.create_user(correo, nombre, apellido, password)
    # modificar valores que son correspondientes a un super usuario
    nuevoUsuario.is_superuser = True
    nuevoUsuario.is_staff = True
    nuevoUsuario.save()

class Usuario(AbstractBaseUser):
  id = models.AutoField(primary_key=True, unique=True)
  nombre = models.CharField(max_length=45)
  apellido = models.CharField(max_length=45)
  correo = models.EmailField(unique=True)
  password = models.TextField()

  # Opcional
  # sirve si se va a utilizar el CMS
  # is_staff indica si el usuario es parte del staff que puede ingresar al CMS
  is_staff = models.BooleanField(default=False)
  # is_active indica si el usuario parte del staff está activo para que ingrese al CMS
  is_active = models.BooleanField(default=True) 

  # python mange.py createsuperuser: comportamiento que va a tener
  objects = ManejoUsuario()

  # para que el login del panel administrativo ;pida el username
  USERNAME_FIELD = 'correo'

  # las columnas que serán requeridas cuando se haga el registro del superusuario por consola
  REQUIRED_FIELDS = ['nombre', 'apellido']

  class Meta:
    db_table = 'usuarios'

