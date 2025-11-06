def recorrerLista(item, nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrerLista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", "")
            print(x)

if __name__ == '__main__':

    lista = ["elemento1n1", "elemento2n1", "elemento3n1",["elemento1n2", "elemento2n2", "elemento3n2",["elemento1n3", "elemento2n3", "elemento3n3"]]]

    recorrerLista(lista)

    print('--NIVEL 1------------------------------------')
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[3])
    print('--NIVEL 2------------------------------------')
    print(lista[3][0])
    print(lista[3][1])
    print(lista[3][2])
    print(lista[3][3])
    print('--NIVEL 3------------------------------------')
    print(lista[3][3][0])
    print(lista[3][3][1])
    print(lista[3][3][2])
    input()