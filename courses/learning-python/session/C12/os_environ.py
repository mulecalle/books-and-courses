import os

#retorna todas las variables de entorno
os.environ.keys()
print(os.environ.keys())


#recupera las variables de entorno en una lista
L = list(os.environ.keys())
print(L)


#recupera la variable de entorno path
os.environ['path']

#El siguiente for recoge e imprime cada contenido en la variable path separandolo mediante el separador que utiliza el sistema operativo.
for srcdir in os.environ['path'].split(os.pathsep):
    print(srcdir)