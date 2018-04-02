from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length = 30, default = "")
    minicodigo = models.CharField(max_length = 10, default = "")
    codigofabricante = models.CharField(max_length = 30, default = "")
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 300)
    categoria = models.CharField(max_length = 100)
    precio = models.FloatField(default = 9.99)
    cadenacaracteristicas = models.TextField(default = "")

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    codigo = models.CharField(max_length = 10, null = True)
    tabladetalle = models.TextField()
    importe = models.FloatField()
    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    nitems = models.IntegerField()
    def __str__(self):
        return self.codigo
