from tkinter import *

master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", state=DISABLED, command=callback)
b.pack()
mainloop()