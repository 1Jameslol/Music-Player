from tkinter import *
from controls import Controls

root = Tk()

class GUI:
    def __init__(self):
        print("constructor called")

        root.title("Audio Player")
        root.geometry('800x800+500+50')
        root.resizable(False, False)
        root.mainloop()

#calls controls constructor
controls = Controls(root)