from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from vistaprevia.models import Producto
from django.shortcuts import redirect
from vistaprevia.forms import CargarForm
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.views.generic import View

"""
def index(request):
    contenido = { 'nombre_sitio': 'LibrosOnline' }
    return render(request, 'vistaprevia/index.html', contenido)
"""

"""
def index(request):
    contenido = { 'nombre_sitio': 'LibrosOnline' }
    para_minorista = { 'tipo_usuario' : 'minorista' , 'incremento' : '25'}
    para_mayorista = { 'tipo_usuario' : 'mayorista' , 'incremento' : '10'}
    return render(request,
	'vistaprevia/index.html', {'contenido':contenido,
	'para_minorista':para_minorista,
	'para_mayorista':para_mayorista})
"""


class Home(View):

    template = 'vistaprevia/index.html'

    def get(self, request, *args, **kwargs):

        params = {}
        params ['para_minorista'] = { 'tipo_usuario' : 'minorista' , 'incremento' : '25'}
        params['para_mayorista'] = { 'tipo_usuario' : 'mayorista' , 'incremento' : '10'}
        return render(request, self.template, params)



"""
def cargar_imagen(request):
    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Producto(producto=request.POST['producto'], fecha_publicacion=request.POST['fecha_publicacion'], ruta_imagen=request.FILES['ruta_imagen'])
            newdoc.save(form)
            return redirect("index")
            # return HttpResponse(newdoc)
    else:
        form = CargarForm()
    return render(request, 'vistaprevia/formulario.html', {'form': form})
"""

class CargarImagen(View):

    template = 'vistaprevia/formulario.html'

    def get(self, request, *args, **kwargs):
        form = CargarForm()
        params = {}
        params ['form'] = form
        return render(request, self.template, params)


    def post(self, request, *args, **kwargs):
        form = CargarForm(request.POST or None)
        params = {}
        params ['form'] = form
        if form.is_valid():
            newdoc = Producto(producto=request.POST['producto'], fecha_publicacion=request.POST['fecha_publicacion'], ruta_imagen=request.FILES['ruta_imagen'])
            newdoc.save(form)
            return redirect("index")





def ver_imagen(request, producto_id):
    """
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    """
    producto = get_object_or_404(Producto, pk=producto_id)
    return render_to_response('vistaprevia/verimagen.html', {
        'producto': producto,
        'error_message': "No has seleccionado un producto.",
    }, content_type=RequestContext(request))


def ver_imagenes(request):
    try:
        productos = Producto.objects.all()
    except Producto.DoesNotExist:
        raise Http404
    return render_to_response('vistaprevia/verimagenes.html', {
        'productos': productos,
        'error_message': "No has seleccionado un producto.",
    }, content_type=RequestContext(request))
