class Vehiculo(object):
    def __init__(self):
        print("Dos ruedas")
        super(Vehiculo,self).__init__()

class Material(object):
    def __init__(self):
        print("plástico")
        super(Material,self).__init__()

class Moto(Vehiculo, Material):
    def __init__(self):
        print("Modelo 1")
        super().__init__()

objeto1 = Moto()
