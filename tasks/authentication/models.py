from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):

  def create_user(self, email, name, lastname, password):
    if not email:
      raise ValueError('An email acccount is required')
    email = self.normalize_email(email)
    newUser = self.model(email=email, name=name, lastname=lastname)
    newUser.set_password(password)
    newUser.save()
    return newUser
  
  def create_superuser(self, email, name, lastname, password):
    newUser = self.create_user(email, name, lastname, password)
    newUser.is_superuser = True
    newUser.is_staff = True
    newUser.save()

class User(AbstractBaseUser):

  id = models.AutoField(primary_key=True, unique=True)
  name = models.CharField(max_length=45)
  lastname = models.CharField(max_length=45)
  email = models.EmailField(unique=True)
  password = models.TextField()

  # Optional (Django CMS)
  is_staff = models.BooleanField(default=
  False)
  is_active = models.BooleanField(default=True)

  objects = UserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [ 'name', 'lastname']

  class Meta:
    db_table = 'users'