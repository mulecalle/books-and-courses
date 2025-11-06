from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Respuesta', message='Hola %s!' % name)

top = Tk()
top.geometry("300x300")
top.title('Echo')
top.iconbitmap('pajaro.ico')
Label(top, text="Ingrese su nombre:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)

# la entrada para reply es <ent.get()>
btn = Button(top, text="Enviar", command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)
top.mainloop()