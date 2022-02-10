from struct import pack
import tkinter as tk
import random
from tkinter import messagebox
from tkinter.messagebox import *
import tkinter

gui = tkinter.Tk()

# alle tkinter code komt hier tussen
gui.title("Grabbelton")
gui.geometry("500x250")
gui.config(bg="yellow")

Random = ["kaas", "banaan", "appel", "kiwi", "aardbei", "5.000.000", "1 euro", "opel corsa 1.2 liter", "lamborghini Urus", "cap"]
gegrabbeld = " "
counter = 10

def grabbel():
    global counter, gegrabbeld
    gegrabbeld = random.choice(Random)
    Random.remove(gegrabbeld)
    counter -= 1
    Frame = tkinter.Label(
        gui,
        text="Gefeliciteerd, je hebt " + (gegrabbeld) +  " gegrabbeld er zijn nog " +str(counter) + " prijzen over!",
        bg="yellow",
    )
    messagebox.showinfo('Random',"Gefeliciteerd, je hebt "+ (gegrabbeld) + " gegrabbeld!")
    Frame.pack()

Button = tk.Button(
text="Grabbel",
font=("arial",25,"bold"),
bg="black",
fg="yellow",
command=grabbel
)
Button.pack()

# alle tkinter code komt hier tussen
gui.mainloop()