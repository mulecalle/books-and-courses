from tkinter import *
master = Tk()

photo=PhotoImage(file="download.gif")
c = Button(master, text="Sure!", anchor=W, justify=LEFT, image=photo )
c.pack(fill=BOTH, expand=1)
mainloop()
