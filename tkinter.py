#tkinter
from tkinter import *
def action():
    print("Hello!")
window = Tk()
a = Button(window, text='Press the button', command=action)
a.pack()

