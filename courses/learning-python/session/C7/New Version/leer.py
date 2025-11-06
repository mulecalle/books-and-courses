from tkinter import *

def CrearFormLeer(root):

    formulario = Frame(root)
    formulario.pack(expand=YES)

    div0 = Frame(formulario, padx=5, pady=5, borderwidth=2, relief='groove')
    div0.pack()

    id_leer = Entry(div0)
    id_leer.config(justify=CENTER, width=40)
    id_leer.pack()

    idVar = StringVar()
    id_leer.config(textvariable=idVar)
    id_leer.bind('<Button-1>', (lambda event: clearEntry(idVar)))

    idVar.set("-- Ingrese el id --")

    return idVar

def clearEntry(arg):
    arg.set("")

if __name__ == '__main__':
    root = Tk()
    vars_leer = CrearFormLeer(root)
    root.bind('<Return>', (lambda event: imprimir(vars_leer)))
    root.mainloop()
