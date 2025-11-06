from django.conf.urls import url

from vistaprevia import views
from vistaprevia.views import Home, CargarImagen

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', Home.as_view(), name='index'),
    #url(r'^cargar/', views.cargar_imagen, name='cargar'),
    url(r'^cargar/', CargarImagen.as_view(), name='cargar'),
    url(r'^(?P<producto_id>\d+)/ver/$', views.ver_imagen, name='ver'),
    url(r'^verimagenes/$', views.ver_imagenes, name='verimagenes'),

]



