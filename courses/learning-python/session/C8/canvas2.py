from tkinter import *
trazo = False


class EventosEnCanvas:
    def __init__(self, parent=None):
        canvas = Canvas(width=350, height=350)
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.crear)
        canvas.bind('<B1-Motion>', self.aumentarDisminuir)
        canvas.bind('<Double-1>', self.borrar)
        canvas.bind('<ButtonPress-3>', self.mover)
        self.canvas = canvas
        self.arrastar = None
        self.tipo = [canvas.create_oval, canvas.create_rectangle]

    def crear(self, event):
        self.forma = self.tipo[0]
        self.tipo = self.tipo[1:] + self.tipo[:1]
        self.inicio = event
        self.arrastar = None

    def aumentarDisminuir(self, event):
        canvas1 = event.widget
        if self.arrastar:
            canvas1.delete(self.arrastar)
        objectId = self.forma(self.inicio.x, self.inicio.y, event.x, event.y)
        if trazo:
            print(objectId)
        self.arrastar = objectId

    def borrar(self, event):
        event.widget.delete('all')

    def mover(self, event):
        if self.arrastar:
            if trazo:
                print(self.arrastar)
            canvas = event.widget
            diffX, diffY = (event.x - self.inicio.x), (event.y - self.inicio.y)
            canvas.move(self.arrastar, diffX, diffY)
            self.inicio = event

if __name__ == '__main__':
    EventosEnCanvas()
    mainloop()
