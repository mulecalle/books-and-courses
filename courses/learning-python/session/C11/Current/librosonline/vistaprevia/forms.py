from django.forms import ModelForm
from .models import Producto


class CargarForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['producto', 'fecha_publicacion', 'ruta_imagen']


        error_messages = {
            'producto': {
                'required': ("Se debe agregar un nombre de producto"),
            },
            'fecha_publicacion': {
                'required': ("Se debe agregar la fecha de publicación en el formato adecuado"),
            },
        }








