def recorrerLista(item):
    for x in item:
        if isinstance(x, list):
            recorrerLista(x)
        else:
            print(x)