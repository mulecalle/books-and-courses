"""from django.contrib import admin
from vistaprevia.models import Producto

admin.site.register(Producto)
"""
from django.contrib import admin
from vistaprevia.models import Producto

class ProductoAdmin(admin.ModelAdmin):
    fields =['fecha_publicacion' , 'producto', 'ruta_imagen']

admin.site.register(Producto, ProductoAdmin)