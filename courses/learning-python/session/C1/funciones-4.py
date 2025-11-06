A = 5
B = 6
def nopisa():
    A = 10
    print('La variable A dentro de la función tiene por valor',A)
    print('B es global, por lo que puedo impirmirla acá', B)

nopisa()
print('La variable A fuera de la función tiene por valor',A)
print('',end='\n################\n' )
+eval(input())
