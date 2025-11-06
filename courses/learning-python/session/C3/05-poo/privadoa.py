class AccesoPrivado(object):

    def __privado(self):
        print("Método privado ")

    def getPrivado(self):
        self.asd = 4
        self.__variableprivada()

objeto = AccesoPrivado()
objeto.getPrivado()
objeto.asd = 8
print(objeto.asd)

objeto._AccesoPrivado__privado()


#g1.__privado()
#Traceback (most recent call last):
#  File "<interactive input>", line 1, in ?
#AttributeError: 'Gato' object has no attribute '__privado'



