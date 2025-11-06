from tkinter import *
from tkinter.messagebox import showinfo

def retorno():
    showinfo(title='Ventana Emergente', message='Se ha presionado el botón!')
# Tk () permite pasar el contenedor como primer agumento
window = Tk()
window.geometry("300x300")
button = Button(window, text='Presionar', command=retorno)
button.pack()
window.mainloop()
