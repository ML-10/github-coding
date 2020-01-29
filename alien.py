from winsound import PlaySound, SND_ASYNC
from tkinter import *
window = Tk()
window.title('Alien')
c = Canvas(window, height=300, width=400)
c.pack()
body = c.create_oval(100, 150, 300, 250, fill='green')
eye = c.create_oval(170, 70, 230, 130, fill='white')
eyeball = c.create_oval(190, 90, 210, 110, fill='black')
mouth = c.create_oval(150, 220, 250, 240, fill='red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')
i = c.itemconfig
def mouth_open():
     i(mouth, fill='black')
def mouth_close():
     i(mouth, fill='red')
def blink():
     i(eyeball, state=HIDDEN)
     i(eye, fill='green')
def unblink():
     i(eyeball, state=NORMAL)
     i(eye, fill='white')
def burp(event):
     mouth_open()
     PlaySound(r'C:\Users\sophi\Desktop\matthews things\python files\__pycache__\__pycache__\alien\burpsnd.wav', SND_ASYNC)
     mouth_close()
c.bind_all('<Button-1>', burp)
