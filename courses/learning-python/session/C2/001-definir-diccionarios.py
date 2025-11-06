import pprint

# #################################################
# Definir diccionarios
# #################################################
def listPrint(aList, anotherList):
    print("[listPrint] START")
    print(aList)
    print(anotherList)
    print("[listPrint] END")
    print('------------------------------')
# #################################################
# Lista de diccionarios
# #################################################
def dictWList(aList, anotherList):
    print("[dictWList] START")
    personas = [aList, anotherList]
    for x in personas:
        print(x['identificacion']['nombre'], '!\n')
    print("[dictWList] END")
    print('------------------------------')
# #################################################
# Diccionario de diccionarios
# #################################################
def DictWDicts(aList, anotherList):
    print("[DictWDicts] START")
    db= {}
    db['Juan'] = aList
    db['Susana'] = anotherList
    print(db['Juan']['identificacion']['nombre'])
    print(db['Susana']['edad'])
    print(db)
    print("[DictWDicts] END")
    print('------------------------------')
# #################################################
# Aumentar legibilidad con modulo pprint
# #################################################
def raiseLog(aList, anotherList):
    print("[raiseLog] START")
    db= {}
    db['Juan']= aList
    db['Susana']= anotherList
    pprint.pprint(db)
    print("[raiseLog] END")
    print('------------------------------')
# #################################################
# Chequear presencia de un elemento
# #################################################
def isIncluded(aList, db):
    print("[isIncluded] START")
    print('identificacion' in aList)
    print('nombre' in aList)
    print('nombre' in db)
    print("[isIncluded] END")
    print('------------------------------')
# #################################################
# Recorrer diccionario (comprension)
# #################################################
def printDict(aList, db):
    print("[printDict] START")
    print([key for (key, value) in db.items()])
    print([value for (key, value) in aList.items() if key == 'identificacion'])
    print([key for key in db.keys()])
    print("[printDict] START")

if __name__ == '__main__':
    Juan = {'identificacion': {'nombre': 'Juan', 'apellido': 'Garcia'}, 'edad': 24, 'sueldo': 5000,'profesion': 'Pintor'}
    Susana = {'identificacion': {'nombre': 'Susana', 'apellido': 'Gomez'}, 'edad': 25, 'sueldo': 6000,'profesion': 'Empleada'}
    db = {}
    db['Juan'] = Juan
    db['Susana'] = Susana

    listPrint(Juan,Susana)
    dictWList(Juan,Susana)
    DictWDicts(Juan,Susana)
    raiseLog(Juan,Susana)
    isIncluded(Juan, db)
    printDict(Juan, db)