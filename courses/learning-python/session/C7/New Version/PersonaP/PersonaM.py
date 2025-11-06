class Persona:

    def __init__(self, nombre, edad, sueldo, trabajo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.trabajo = trabajo

    def apellido(self):
        return self.nombre.split()[-1]

    def darAumento(self, porcentaje):
        self.sueldo *= (1.0 + porcentaje)

    def setNombre(self, newName):
        self.nombre = newName

    def setEdad(self, newAge):
        self.edad = newAge

    def setSueldo(self, newFee):
        self.sueldo = newFee

    def setTrabajo(self, newPosition):
        self.trabajo = newPosition

    def __str__(self):
        return ('%s details: \nNombre: %s \nEdad: %s \nSueldo: %s\nTrabajo: %s' %
            (self.__class__.__name__, self.nombre, self.edad, self.sueldo, self.trabajo))

if __name__ == '__main__':
    Juan = Persona('Juan Garcia', 42, 30000, 'software')
    Susana = Persona('Susana Gomez', 45, 40000, 'hardware')
    print(Juan.nombre, Susana.sueldo)
    print(Juan.apellido())
    Susana.darAumento(0.10)
    print(Susana.sueldo)