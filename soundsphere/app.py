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
from os import *

BROWSER = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()

url = "https://www.soundcraft.com/ui-demo/mixer.html"

label = Label(root, text="Closing this window will cause chrome to run\n"+url)
label.pack()

app = Window(root)
root.mainloop()

run_string = BROWSER+" -url "+url+" --kiosk"

print (run_string)

#os.system(BROWSER+" -ulr \""+url+"\" --kiosk")
