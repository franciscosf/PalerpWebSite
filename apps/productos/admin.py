from django.contrib import admin
from apps.productos.models import Producto
from apps.productos.models import Compra

# Register your models here.

admin.site.register(Producto)
admin.site.register(Compra)
