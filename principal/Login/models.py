from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# En CustomUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        rol_id = extra_fields.pop('id_rol', None)
        if rol_id:
            extra_fields['id_rol'] = Rol.objects.get(pk=rol_id)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)  # Cambiado a EmailField para validar correos
    direccion = models.CharField(max_length=30)
    genero = models.CharField(max_length=15)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    # Define el campo que se usará como nombre de usuario
    USERNAME_FIELD = 'username'

    # Define los campos que son requeridos para crear un superusuario
    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono', 'email', 'direccion', 'genero', 'password', 'id_rol']

    objects = CustomUserManager()  # Usar el CustomUserManager

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'

    def get_short_name(self):
        return self.nombre

class Rol(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre


                