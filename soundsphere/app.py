#!/usr/bin/env python

__author__ = "Jakub Malec"
__copyright__ = "Copyright 2019, Jakub Malec"
__credits__ = ["Jakub Malec"]

__license__ = "MIT"
ersion__ = "0.1"
__maintainer__ = "Jakub Malec"
__email__ = "jakub.malec@outlook.com"
__status__ = "Dev"

from Tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
app = Window(root)
root.mainloop()

