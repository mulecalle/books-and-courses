from tkinter import *


class MiApp:

    def __init__(self, parent=None, **configs):
        # ##################################################################
        # Ventana principal
        # ##################################################################
        self.myParent = parent
        self.myParent.geometry("700x600")


if __name__ == '__main__':
    root = Tk()
    MiApp(root)
    root.mainloop()



