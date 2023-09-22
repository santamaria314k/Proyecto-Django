from django.db import models

# Create your models here.


class Usuario(models.Model):
    id_user = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    genero = models.CharField(max_length=15)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Rol(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre
