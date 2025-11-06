from django.conf.urls import url

from vistaprevia import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

]



