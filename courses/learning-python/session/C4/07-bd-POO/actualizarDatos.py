import shelve
from PersonaP.PersonaM import Persona
from GerenteP.GerenteM import Gerente

Juan = Persona('Juan Garcia', 42)
Susana = Persona('Susana Gomez', 45, 40000)
Tom = Gerente('Tom Perez', 42, 50000)

db = shelve.open('persona')
Tom = db['Tom']
Tom.darAumento(0.20)
db['Tom'] = Tom
db.close()
