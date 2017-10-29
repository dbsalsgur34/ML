import tkinter

from tkinter import *

mainWindow = Tk()
mainWindow.title = "hw1"

frame = Frame(mainWindow)
frame.pack()
lbl = Label(frame, text="name")
lbl.pack()
txt = Entry(frame)
txt.pack()
btn = Button(frame, text="OK", width=15)
btn.pack()
image = PhotoImage(file="2.gif")
label = Label(mainWindow, image=image)
label.pack()

mainWindow.mainloop()