from tkinter import *
import time as t


index = 0

def update():
    global index
    index += 1
    lettres = ["a","b","c","d","e"]
    lettre = lettres[index%5]
    lbl.config(text=lettre)
    t.sleep(1)
    root.after(10, update)

root = Tk()
lbl = Label(root, text='0')
lbl.pack()
my_button = Button(root, text='Start showing lettre', command=update)
my_button.pack()
root.mainloop()