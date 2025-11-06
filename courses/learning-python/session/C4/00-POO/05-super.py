class Vehiculo():
    def tipo(self):
        print("Dos ruedas")

class Material():
    def tipo(self):
        print("plástico")

class Moto(Vehiculo, Material):
    def modelo(self):
        print("Modelo 1")
        super().tipo()
        Material.tipo(self)
        Vehiculo.tipo(self)

class Bicicleta(Material, Vehiculo):
    def modelo(self):
        print("Modelo 2")
        super().tipo()
        Material.tipo(self)
        Vehiculo.tipo(self)


print("---------- para objeto 2 ------------")
objeto2 = Bicicleta()
objeto2.modelo()
#objeto2.tipo()
