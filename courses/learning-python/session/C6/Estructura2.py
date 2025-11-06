from tkinter import *


class MiApp:

    def __init__(self, parent=None, **configs):
        # ##################################################################
        # Ventana principal
        # ##################################################################
        self.myParent = parent
        self.myParent.geometry("700x600")
        # ##################################################################
        # Agrego contenedor
        # ##################################################################
        self.Contenedor = Frame(self.myParent, bg="#444")
        self.Contenedor.pack(expand=YES, fill=BOTH)

if __name__ == '__main__':
    root = Tk()
    MiApp(root)
    root.mainloop()

