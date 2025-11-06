##The view knows nothing about the controller or the model.

# Modules out house
from tkinter import *
import threading
import time
class View(threading.Thread):

    # Variable to shown
    currentFunction=''
    time=''
    passCount=''
    failCount=''
    skipCount=''

    def __init__(self):

        # initialize a thread focus at the gui
        threading.Thread.__init__(self)
        self.thread = threading.current_thread()

        # initialize the variables to shown
        self.currentFunction = ''
        self.time = '0'
        self.passCount = '0'
        self.failCount = '0'
        self.skipCount = '0'

        self.asd = self.start()

        self.condition = threading.Condition()

        self.condition.acquire()


    def run(self):

        # build and show the gui
        self.root = Tk()
        self.root.withdraw()
        
        self.gui = Toplevel(self.root)

        self.currentRunning = Label(self.gui, text=self.currentFunction, borderwidth=1, relief="ridge").pack(side=BOTTOM, fill=BOTH)
        self.remTime = Label(self.gui, text=self.time, borderwidth=1, relief="ridge").pack(side=BOTTOM, fill=BOTH)
        self.p = Label(self.gui, text=self.passCount, borderwidth=1, bg="green", relief="ridge", width='5').pack(side=LEFT, fill=BOTH)
        self.f = Label(self.gui, text=self.failCount, borderwidth=1, bg="red", relief="ridge", width='5').pack(side=RIGHT, fill=BOTH)
        self.s = Label(self.gui, text=self.skipCount, borderwidth=1, bg="yellow", relief="ridge", width='5').pack(side=BOTTOM, fill=BOTH)

        # remove windows buttons from the app
        self.gui.overrideredirect(True)

        # set the app the windows position
        self.gui.geometry('%dx%d+%d+%d' % (100, 56, 1163, 74))

        # set the app transparency
        self.gui.wm_attributes('-alpha', 0.5)

        # set the app always on top
        self.gui.wm_attributes("-topmost", 1)

        self.gui.mainloop()

    def update_content(self, dict_state):

        print('[update_content] START')

        # receive the content at the model and then update the view
        self.time = dict_state['TTend']
        self.currentFunction = dict_state['function']
        self.passCount = dict_state['pass']
        self.failCount = dict_state['fail']
        self.skipCount = dict_state['skip']
