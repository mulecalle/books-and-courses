from PersonaP.PersonaM import Persona


class Gerente(Persona):

    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad, sueldo, 'Gerente')

    def darAumento(self, porcentaje, premio=0.1):
        Persona.darAumento(self, porcentaje + premio)

