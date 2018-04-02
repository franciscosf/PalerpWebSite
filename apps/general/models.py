from django.db import models

# Create your models here.

class PosibleCliente(models.Model):
    RUC = models.CharField(max_length = 12)
    nombre = models.CharField(max_length = 100)
    email = models.CharField(max_length = 150)
    telefono = models.CharField(max_length = 15)

    def __str__(self):
        return self.RUC
