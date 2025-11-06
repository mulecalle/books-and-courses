from tkinter import *

master = Tk()

b = Button(master, text="Ok!", anchor=W, justify=LEFT, padx=22,
     height=3, width=12, font=('courier', 22, 'bold'))
b.pack(fill=BOTH, expand=1)
mainloop()
