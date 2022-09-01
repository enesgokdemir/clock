from tkinter import *
from time import *
import datetime

root = Tk()
root.title("Clock")


def clock():
    text = strftime("%H:%M:%S")
    label.config(text=text)
    label.after(1000, clock)


label = Label(root, font=("ds-digital", 100), background="#FFB6C1", foreground="white")
label.pack(anchor="center")

clock()
mainloop()
