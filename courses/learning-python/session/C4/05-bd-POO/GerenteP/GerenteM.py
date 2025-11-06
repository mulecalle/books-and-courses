from PersonaP.PersonaM import Persona


class Gerente(Persona):

    def darAumento(self, porcentaje, premio=0.1):
        self.sueldo *= (1.0 + porcentaje + premio)