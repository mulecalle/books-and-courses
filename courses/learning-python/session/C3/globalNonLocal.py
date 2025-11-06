nivel0 = 0

def f1():

    global nivel0
    nivel0 = "mod0"
    nivel1 = 1

    def f2():
        global nivel1
        nivel1 = "mod1"
        nivel2 = 2
        print("lvl 2:" , nivel0, nivel1, nivel2)

    f2()
    print("lvl 1:" , nivel0, nivel1)

f1()
print("lvl 0:" , nivel0)
