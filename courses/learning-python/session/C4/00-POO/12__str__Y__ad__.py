# ###############################
# Clase padre
# ###############################
class PrimerClase:
    def imprimir(self):
        print((self.data))
# ###############################
# Clase hija
# ###############################
class SegundaClase(PrimerClase):
    def imprimir(self):
        print(('Valor actual = "%s"' % self.data))
# ###############################
# Clase nieta
# ###############################
class TerceraClase(SegundaClase):

    def __init__(self, valor):
        self.data = valor

    def __add__(self):
        return '[Esto se imprimer al hacer un print del objeto: %s]' % self.data


objeto1 = TerceraClase('hola')
objeto2 = TerceraClase('hola')
objeto2 = objeto2 + objeto1
print(objeto2)