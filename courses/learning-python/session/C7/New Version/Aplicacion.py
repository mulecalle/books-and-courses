from tkinter import *
from guardarModal import guardar
from leerModal import leer
from cerrar import Cerrar
from viewDelete import deleteFrame
from viewModify import modifyFrame

class MiApp:

    def __init__(self, parent=None, **configs):


        # ################# #
        # Ventana principal #
        # ################# #
        self.myParent = parent
        self.myParent.geometry("400x300")


        # ################# #
        # Agrego contenedor #
        # ################# #
        self.Contenedor = Frame(self.myParent)
        self.Contenedor.pack(expand=YES, fill=BOTH)


        #####  SECCIÓN CONTROLES #####
        self.header = Frame(self.Contenedor, relief=RAISED)
        self.header.pack(side=TOP, expand=NO, fill=BOTH)

        Label(self.header, text="Controles", bg="gray", fg="black", relief="solid", justify=LEFT).pack(side=TOP, expand=YES, fill=X, anchor=W)

        self.body = Frame(self.Contenedor)
        self.body.pack(side=TOP, pady=25)

        saveButton = Button(self.body, text='Guardar', command=guardar, height="2", width="7").pack()
        viewButton = Button(self.body, text='Ver', command=leer, height="2", width="7").pack()
        modifyButton = Button(self.body, text='Modify', command=modifyFrame, height="2", width="7").pack()
        deleteButton = Button(self.body, text='Delete', command=deleteFrame, height="2", width="7").pack()
        widget = Button(self.body, text='Cerrar', command=Cerrar, height="2", width="7").pack()


if __name__ == '__main__':
    root = Tk()
    MiApp(root)
    root.mainloop()