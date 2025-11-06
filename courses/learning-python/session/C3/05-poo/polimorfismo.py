class ClasePadre1:
    atributo1 = 2

    def imprimir(self, nombre):
        self.nombre=nombre
        print("Este es un nombre: " + self.nombre)

class ClaseHija(ClasePadre1):
    atributo2 = 4

    def imprimir(self, nombre):
        self.nombre=nombre
        print(self.nombre)

objeto1 = ClasePadre1()
print(objeto1.atributo1)
objeto1.imprimir('Juan')

objeto2 = ClaseHija()

objeto2.imprimir('Marcelo')

