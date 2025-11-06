from tkinter import *

win = Tk()
imagen = PhotoImage(file="img/" + "download.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=imagen, anchor=NW)
win.mainloop()

