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
import os

class UpdaterWindow(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("SoundSphere Update")
        self.master.geometry("400x200")
        self.master.resizable(False, False)


def update():
    print("done")


root = Tk()


update_button = Button(root, text="Update", command = update)
update_button.pack()




app = UpdaterWindow(root)
root.mainloop()
