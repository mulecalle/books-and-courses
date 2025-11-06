import sys
from tkinter import Toplevel, Button, Label
ventana1 = Toplevel()
ventana2 = Toplevel()
Button(ventana1, text='Botón ventana 1', command=sys.exit).pack()
Button(ventana2, text='Botón ventana 2', command=sys.exit).pack()
Label(text='Ventana por defecto').pack()
ventana1.mainloop()

