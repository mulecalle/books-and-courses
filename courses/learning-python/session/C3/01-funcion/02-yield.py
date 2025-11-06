# ##############################################
# Ejemplo 1 - Uso de yield ####
# ##############################################
def contador_yield1(max):
    print('asd'+str(max))
    n=0
    while n < max:
        print('a'+ str(n))
        yield n
        print('b' + str(n))
        n+=1
        print('c' + str(n))

d = contador_yield1(3)

print(d)
print('---')
next(d)
print('---')
next(d)
print('---')
print(next(d))
print('---')
print(d)

