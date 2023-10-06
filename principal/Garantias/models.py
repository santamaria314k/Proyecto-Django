from django.db import models

# Create your models here.


class TiposGarantia(models.Model):
    id_tiga = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

#----------------------------------------------------------------------------------------


class Garantias(models.Model):
    id_gar = models.AutoField(primary_key=True)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    id_serveh = models.ForeignKey(Serviciosxvehiculos, on_delete=models.CASCADE)
    id_tiga = models.ForeignKey(TiposGarantia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Garantia {self.id_gar}"






