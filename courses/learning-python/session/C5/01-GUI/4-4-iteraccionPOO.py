from tkinter import *
from tkinter.messagebox import showinfo


class PrimerApp():
    def __init__(self, parent=None):

        self.myParent = parent
        self.myParent.geometry("300x300")
        self.myParent.title('Echo')
        self.myParent.iconbitmap('pajaro.ico')

        Label(self.myParent, text="Ingrese su nombre:").pack(side=TOP)
        ent = Entry(self.myParent)
        ent.pack(side=TOP)

        button = Button(self.myParent,  text="Enviar", command=(lambda: retorno(ent.get())))
        button.pack(side=LEFT)

        def retorno(name):
            showinfo(title='Respuesta', message='Hola %s!' % name)

if __name__ == '__main__':
    root = Tk()
    myapp = PrimerApp(root)
    root.mainloop()