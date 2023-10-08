from django.db import models

# Create your models here.
from django.db import models
from Login.models import Usuario
from Valoracion.models import Diagnostico


# Create your models here.
class Vehiculos(models.Model):
    id_veh = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=15)
    lugarExpediplaca = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    año = models.IntegerField()
    modelo = models.CharField(max_length=25)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_val = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)


    def __str__(self):
        return f"Vehiculo {self.id_veh}"


#----------------------------------------------------------------------------------------




class Servicios(models.Model):
    id_ser = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return self.nombre


#----------------------------------------------------------------------------------------


class Serviciosxvehiculos(models.Model):
    id_serveh = models.AutoField(primary_key=True)
    id_veh = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    id_ser = models.ForeignKey(Servicios, on_delete=models.CASCADE)


    def __str__(self):
        return f"Servicio {self.id_ser} para Vehiculo {self.id_veh}"
     