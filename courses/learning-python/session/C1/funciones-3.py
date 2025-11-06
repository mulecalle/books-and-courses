A = 5               # A es global

def sumarCinco(B):
    C = A + B     # B y C son locales a la función
    return C

print(sumarCinco(5))
+eval(input())
