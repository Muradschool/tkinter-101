import tkinter
from tkinter.tix import Tk
from turtle import color

window = tkinter.Tk()

# alle tkinter code komt hier tussen
window.title('Hello.py')
window.geometry('100x100')
window.config(bg='blue')

box1 = tkinter.Label(
    window,
    text="Hello Tkinter!", 
    bg="green",
    fg="yellow"        
)

box1.pack(
    ipadx=10,
    ipady=10
)

# alle tkinter code komt hier tussen
window.mainloop()