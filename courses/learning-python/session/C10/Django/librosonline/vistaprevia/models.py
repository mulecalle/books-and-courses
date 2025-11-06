from django.db import models

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    ruta_imagen = models.FileField(upload_to='fotos/%Y/%m/%d',default='defecto/defecto.png', blank=True, null=True)

    def __str__(self):
        return ('<%s => %s: %s, %s>' % (self.__class__.__name__, self.producto, self.fecha_publicacion, self.ruta_imagen))