import tkinter
import time

# alle tkinter code komt hier tussen 
gui = tkinter.Tk()
gui.title("Clock")
gui.geometry("500x200")

def tijd():
    current_time = time.strftime("%H:%M:%S")
    clock.configure(text= current_time)
    clock.after(200,tijd)

clock = tkinter.Label(
    gui,
    font=("Symbol",100),
    bg="black",
    fg="yellow",

)
clock.pack(
    fill="both",
    padx=0,
    pady=0,
    expand=True
)

tijd() 
gui.mainloop()
# alle tkinter code komt hier tussen 
