if __name__ == '__main__':
    # #######################################################
    # OJOOOOOOOOOOO COMO DEBO LLAMAR A LA CLASE PADRE
    # EN EL MÓDULO DE LA CLASE HIJA PARA QUE FUNCIONE
    # AL LLAMAR LA CLASE HIJA DESDE FUERA
    # DEBO CONSIDERAR DONDE ESTOY PARADO OJOOOOOOOOOOOOO
    # #######################################################
    from datosInicioP.PersonaM import Persona
    from datosInicioP.GerenteM import Gerente
    Juan = Persona('Juan Garcia', 42)
    Susana = Persona('Susana Gomez', 45, 40000)
    Tom = Gerente('Tom Perez', 42, 50000, 'software')
    personas = [Juan, Susana, Tom]
    for persona in personas:
        print(persona.nombre, persona.sueldo)
    print('-----------------------')
