from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    fields =['fecha_publicacion', 'producto']

admin.site.register(Producto)