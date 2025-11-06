# ##############################################
#  ####
# ##############################################
nivel0 = 0
nivel1 = 1
def f1():
    global nivel1
    nivel1 = 4

    def f2():
        global nivel1
        print(nivel1)
        nivel2 = 2
        nivel1 = 3
        print('print en f2::::'+ str(nivel0) +str(nivel1) + str(nivel2))

    f2()

    print('print en f1::::'+ str(nivel0)+ str(nivel1))

f1()


print(nivel0,nivel1)
