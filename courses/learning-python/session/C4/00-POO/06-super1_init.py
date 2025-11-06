class Vehiculo():
    def __init__(self):
        print("Dos ruedas")
        super().__init__()

class Material():
    def __init__(self):
        print("plástico")
        super().__init__()

class Pepito():
    def __init__(self):
        print("pepito")
        super().__init__()

class Moto(Material, Vehiculo, Pepito):
    def __init__(self):
        print("Modelo 1")
        Vehiculo.__init__(self)
        print('--')
        Material.__init__(self)

objeto1 = Moto()
print(dir(Moto))
