"""librosonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from vistaprevia import views

urlpatterns = [
    url(r'^vistaprevia/', include('vistaprevia.urls')),
    url(r'^cargar/', views.cargar_imagen, name='cargar'),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<producto_id>\d+)/ver/$', views.ver_imagen, name='ver'),
    url(r'^verimagenes/$', views.ver_imagenes, name='verimagenes'),
]
