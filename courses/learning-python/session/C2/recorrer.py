def recorrerLista1(currentList, nivel):

    for listItem in currentList:
        if isinstance(listItem, list):
            recorrerLista1(listItem, nivel + 1)
        else:
            for y in range(nivel):
                print((''))
            print(listItem)

def recorrerLista2(currentList, nivel):

    for listItem in currentList:
        if isinstance(listItem, list):
            recorrerLista2(listItem, nivel + 1)
        else:
            for y in range(nivel):
                print(" ")
            print(listItem)

aList = ["elemento1n1", "elemento2n1", "elemento3n1",["elemento1n2", "elemento2n2", "elemento3n2",["elemento1n3", "elemento2n3", "elemento3n3"]]]

recorrerLista2(aList, 0)

