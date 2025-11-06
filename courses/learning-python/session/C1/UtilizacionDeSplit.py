"""
split se utiliza para separar un string por aquellos separadores
que indiquemos, en el siguente ejemplo como los elementos de manzana
están uno a continuación del otro al realizar un print con un
espacio dentro del split toma toda la palabra como un único elemento de lista
"""
a = "Manzana"
print(a.split(" "))
"""
pero si los elementos se encontraran separados por un espacio o una coma
podría recogerlos dentro de una lista cuyos elementos son las letras de la
palabra
"""
a = "M a n z a n a"
print(a.split(" "))

a = "M,a,n,z,a,n,a"
print(a.split(","))
"""
esto se utiliza mucho por ejemplo cuantro quiero tratar con rutas
y necesito quedarme con una parte de la misma, como se puede ver a
continuación.
"""
a = "rutaRaíz/directorio1/directorio2/archivo.py"
b = a.split("/")
print(b)
print(b[3])