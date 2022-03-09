from ast import Lambda
from tkinter import *
import time as t
from functools import partial
import tkinter


class GUI():
    def __init__(self, wight: int, lenght: int):
        self.wight = wight
        self.lenght = lenght
        self.grid


        


    def fibre(self):
        pass

    def graph(self):
        pass

    def csv(self):
        pass


index = 0


def update():
    global index
    index += 1
    lettres = ["a","b","c","d","e"]
    lettre = lettres[index%5]
    label.config(text=lettre)
    label2.config(text=index)
    # t.sleep(0.01)
    window.after(10, update)



window = Tk()
window.geometry()
#Test of the update fonction
label = Label(window, text='Start')
label2 = Label(window, text='Start')
label.pack()
label.config(text="Hello wordl!")
label2.pack()
my_button = Button(window, text='Start showing lettre', command=update)
my_button.pack()

# Apply some new text in the window
def apply():
    print(entry.get)
    label3.config(text=entry.get())

label3 = Label(window,text="Try to input texte")
label3.pack()
entry = Entry(window)
entry.pack()
# button2 = Button(window,text="show the entry", command=show(entry))
button2 = Button(window,text="Show the entry", command=apply)
button2.pack()

# Create continus frame to draw the fiber
lenght = 0
wight = [1,2,1,2,1,2,1,2,1,2,1,2]
def is_new_value():
    return False

def new_value():
    return 0

def draw_the_fiber(height = 0, wight = []):
    if is_new_value():
        wight.append(new_value())
    canvas.create_line(height+100,0,height+100, wight[height])
    if height < len(wight):
        height += 1
        draw_the_fiber(height, wight)


    
canvas = Canvas(window)
button4 = Button(window,text="Print the fiber", command=partial(draw_the_fiber, 0, wight))
button4.pack()
canvas.pack()


window.mainloop()