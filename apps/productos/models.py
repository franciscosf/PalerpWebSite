from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length = 30, default = "")
    minicodigo = models.CharField(max_length = 10, default = "")
    codigofabricante = models.CharField(max_length = 30, default = "")
    nombre = models.CharField(max_length = 100)
    imagen = models.CharField(max_length = 20, default = "noimage.jpg")
    descripcion = models.CharField(max_length = 300)
    categoria = models.CharField(max_length = 100)
    precio = models.FloatField(default = 9.99)
    cadenacaracteristicas = models.TextField(default = "")

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    codigo = models.CharField(max_length = 10, null = True)
    tabladetalle = models.TextField()
    pagado = models.BooleanField( default = False)
    importe = models.FloatField()
    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    nitems = models.IntegerField()
    ####Campos proporcionados por PAYTOPERU
    #INICIO
    froma_pago = models.CharField(max_length = 21, null = True)
    medio_pago = models.CharField(max_length = 21, null = True)
    numero_pedido = models.IntegerField(null = True)
    codigo_autorizacion = models.CharField(max_length = 11, null = True)
    numero_tarjeta = models.CharField(max_length = 24, null = True)
    nombre_tarjeta_habiente = models.CharField(max_length = 201, null = True)
    email = models.CharField(max_length = 150, null = True)
    fecha = models.DateTimeField(null = True)
    #FIN

    def __str__(self):
        return self.codigo
