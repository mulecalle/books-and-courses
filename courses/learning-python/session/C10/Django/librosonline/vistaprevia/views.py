from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render_to_response

from .models import Producto
from .forms import CargarForm

# Create your views here.
def index(request):

    contenido = { 'nombre_sitio': 'LibrosOnline'}
    para_minorista = {'tipo_usuario': 'minorista', 'incremento': '25'}
    para_mayorista = {'tipo_usuario': 'mayorista', 'incremento': '10'}

    return render(request,
                  'vistaprevia/index.html', {'contenido': contenido,
                                             'para_minorista': para_minorista,
                                             'para_mayorista': para_mayorista})


def cargar_imagen(request):

    form = ''

    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)

    if form.is_valid():
        newdoc = Producto(producto=request.POST['producto'], fecha_publicacion=request.POST['fecha_publicacion'], ruta_imagen=request.FILES['ruta_imagen'])
        newdoc.save(form)
        return redirect("index")
    else:
        form = CargarForm()
        return render(request, 'vistaprevia/formulario.html', {'form': form})


def ver_imagen(request, producto_id):

    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404

    return render_to_response('vistaprevia/verimagen.html', {'producto': producto,'error_message': "No has seleccionado un producto.",},content_type=RequestContext(request))

def ver_imagenes(request):

    try:
        productos = Producto.objects.all()
    except Producto.DoesNotExist:
        raise Http404

    return render_to_response('vistaprevia/verimagenes.html', {'productos': productos,'error_message': "No has seleccionado un producto.",},content_type=RequestContext(request))