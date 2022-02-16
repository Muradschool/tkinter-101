from distutils.command.config import config
import tkinter
import tkinter as tk
from tkinter import font

global up
clicks = 0
# alle tkinter code komt hier tussen
gui = tk.Tk()

gui.title("Clicker V1")
gui.geometry("500x500")
gui.config(bg= "gray")
clicks = 0 

def Colors():
    if clicks < 0:
        gui.config(bg= "Red")
    elif clicks > 0:
        gui.config(bg= "Green")
    else:
        gui.config(bg= "Gray")

def up():
    global clicks
    clicks += 1
    Button.config(text=clicks)
    print(clicks)


#box 1
ButtonUp = tk.Button(
text="Up",
font=("arial",25,"bold"),
bg="white",
fg="black",
command=lambda: [up(),Colors()]
)
ButtonUp.pack()

def UpButton():
    print(clicks)
ButtonUp.bind("<Button-1>")

def down():
    global clicks
    clicks -= 1
    Button.config(text=clicks)
    print(clicks)
ButtonUp.bind("<Button-1>")


#box 2
ButtonDown = tk.Button(
text="Down",
font=("arial",25,"bold"),
bg="white",
fg="black",
command=lambda :[down(),Colors()]
)
ButtonDown.place(relx=.5, rely=.5, anchor="s")


#box 3
Button = tk.Label(
text=clicks,
font=("arial",25,"bold"),
bg="white",
fg="black",
)
Button.place(relx=.5, rely=.3, anchor="center")

# alle tkinter code komt hier tussen
gui.mainloop()