import tkinter

window = tkinter.Tk()

# alle tkinter code komt hier tussen 
window.title('My First Window')

grote = 150
y = 0
Colors = ('yellow', 'green', 'blue', 'red', 'orange', 'black')
z = len(Colors)

def changer():
    global grote, window, y, z 
    if z != 0:
        window.geometry(str(grote) +'x'+ str(grote))
        grote = int(grote) +50
        window.configure(bg=Colors[y])
        y = y + 1
        print(z)
        z = z - 1
    else:
        print('Biem!')
        window.destroy()

for x in range(0,len(Colors) + 1):
    window.after(x* 2000, changer)

window.mainloop()
# alle tkinter code komt hier tussen 

