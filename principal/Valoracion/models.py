from django.db import models

# Create your models here.

class Diagnostico(models.Model):
    id_val = models.AutoField(primary_key=True)
    diagnostico = models.CharField(max_length=8000)
    

    def __str__(self):
        return f"ID: {self.id_val}, Diagnostico: {self.diagnostico}"
