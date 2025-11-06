from tkinter import *
from tkinter.messagebox import showinfo


class PrimerApp(Frame):
    def __init__(self, parent=None):

        self.myParent = parent
        self.myParent.geometry("300x300")

        button = Button(self.myParent, text='Presionar', command=self.retorno)
        button.pack()

    def retorno(self):
        showinfo(title='Ventana Emergente', message='Se ha presionado el botón!')

if __name__ == '__main__':
    root = Tk()
    myapp = PrimerApp(root)
    root.mainloop()
