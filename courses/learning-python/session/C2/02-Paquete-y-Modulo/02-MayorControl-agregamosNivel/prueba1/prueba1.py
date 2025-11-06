def recorrerLista(item, nivel):
    for x in item:
        if isinstance(x, list):
            recorrerLista(x, nivel + 1)
        else:
            for y in range(nivel):
                print((''))
            print(x)
