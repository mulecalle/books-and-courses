from tkinter import *

master = Tk()
master.geometry("300x300")
def callback():
    print("click!")
b = Button(master, text="OK", command=callback,
    activebackground="green", activeforeground="yellow",
    background="black", foreground="red", height=7, width=12, anchor=SW)
b.pack(side=LEFT)
mainloop()