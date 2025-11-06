from tkinter import *

master = Tk()
def callback():
    print("click!")
b = Button(master, text="OK", command=callback, padx=132, pady=132)
b.pack()
mainloop()