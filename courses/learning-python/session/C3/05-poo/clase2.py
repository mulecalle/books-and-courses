class ClasePadre1:
    atributo1 = 2

class ClasePadre2:
    atributo1 = 3

class ClaseHija(ClasePadre1, ClasePadre2):
    atributo3 = 4

    def imprimir(self, nombre):

        self.nombre=nombre

        print(self.nombre)


objeto = ClaseHija()

ob
