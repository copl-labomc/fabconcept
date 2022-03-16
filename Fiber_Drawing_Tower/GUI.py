from ast import Lambda
from tkinter import *
import time as t
from functools import partial
from turtle import color


class GUI_TourAFibre:
    def __init__(self):
        self.root = Tk()
        self.root.title("Optical fiber drawing tower")
        # Entry
        self.entryChosenDiametre = Entry(self.root)
        self.entryChosenDiametre.grid(column=3, row=3)
        self.entryNameOfFile = Entry(self.root, text='Name of the file')
        self.entryNameOfFile.grid(column=5, row=1)
        # Labels
        self.labelDiametre = Label(self.root, text='Diameter:')
        self.labelDiametre.grid(column=4, row=3)
        self.labelDiametrePrint = Label(self.root, text='None')
        self.labelDiametrePrint.grid(column=5, row=3)
        self.labelDiametreUnit = Label(self.root, text='mm')
        self.labelDiametreUnit.grid(column=6, row=3)
        self.labelSpeed = Label(self.root, text='Motor speed:')
        self.labelSpeed.grid(column=4,row=2)
        self.labelSpeedPrint = Label(self.root, text='None')
        self.labelSpeedPrint.grid(column=5, row=2)
        self.labelSpeedUnit = Label(self.root, text='m/s')
        self.labelSpeedUnit.grid(column=6,row=2)
        self.labelLenght = Label(self.root, text='Lenght:')
        self.labelLenght.grid(column=4,row=4)
        self.labelLenghtPrint = Label(self.root, text='None')
        self.labelLenghtPrint.grid(column=5, row=4, )
        self.labelLenghtUnit = Label(self.root, text='m')
        self.labelLenghtUnit.grid(column=6,row=4)
        self.labelNameOfFile = Label(self.root, text='File name:')
        self.labelNameOfFile.grid(column=4, row=1)
        self.labelNameOfFileType = Label(self.root, text='.csv')
        self.labelNameOfFileType.grid(column=6, row=1)
        # Buttons
        self.boutonDiametre = Button(self.root, text='Apply', command=self.applyChosenDiametre)
        self.boutonDiametre.grid(column=2, row=3)
        self.boutonStart = Button(self.root, text='Start', command=self.startToCalculat)
        self.boutonStart.grid(column=4, row=6)
        # Canvas
        self.canvasHeight = 100
        self.canvasWidth = 400
        self.canvasFiber = Canvas(self.root, bg='green', height=self.canvasHeight, width=self.canvasWidth)
        self.canvasFiber.grid(column=0, row=6)
        # Slider
        self.sliderScale = Scrollbar(self.root)
        # Graph
        # TO DO

        self.root.mainloop()

    def applyChosenDiametre(self):
        self.labelDiametrePrint.config(text=self.entryChosenDiametre.get())

    def startToCalculat(self):
        self.start = True
        self.labelLenghtPrint.config(text=self.getLenght())
        self.labelSpeedPrint.config(text=self.getMotorSpeed())

    def getLenght(self):
        pass

    def getMotorSpeed(self):
        pass




        

GUI_TourAFibre()


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