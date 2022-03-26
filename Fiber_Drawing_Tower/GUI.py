from tkinter import *
from Arduino_control import *
import random


class GUI_TourAFibre:
    def __init__(self,):
        self.widths = []
        self.values = []
        self.lenght = 0
        self.refrechTime = 100
        # self.arduino = Control('/dev/cu.usbmodem2101')
        self.root = Tk()
        self.root.title("Optical fiber drawing tower")
        # Entry
        self.entryChosenDiametre = Entry(self.root)
        self.entryChosenDiametre.grid(column=3, row=3)
        self.entryNameOfFile = Entry(self.root, text='Name of the file')
        self.entryNameOfFile.grid(column=5, row=1)
        # Labels
        self.labelDiametre = Label(self.root, text='Set Diameter:')
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
        self.labelWidth = Label(self.root, text='Width:')
        self.labelWidth.grid(column=4,row=5)
        self.labelWidthPrint = Label(self.root, text='None')
        self.labelWidthPrint.grid(column=5, row=5, )
        self.labelWidthUnit = Label(self.root, text='mm')
        self.labelWidthUnit.grid(column=6,row=5)
        self.labelNameOfFile = Label(self.root, text='File name:')
        self.labelNameOfFile.grid(column=4, row=1)
        self.labelNameOfFileType = Label(self.root, text='.csv')
        self.labelNameOfFileType.grid(column=6, row=1)
        # Buttons
        self.buttonDiametre = Button(self.root, text='Apply', command=self.applyChosenDiametre)
        self.buttonDiametre.grid(column=2, row=3)
        self.buttonStartStop = Button(self.root, text='Start', command=self.start_stop)
        self.buttonStartStop.grid(column=4, row=6)
        # Canvas
        self.canvasHeight = 100
        self.canvasWidth = 400
        self.canvasFiber = Canvas(self.root, bg='grey', height=self.canvasHeight, width=self.canvasWidth)
        self.canvasFiber.grid(column=0, row=6)
        # Slider
        self.sliderScale = Scrollbar(self.root)
        # CheckButton
        self.check = IntVar()
        self.checkButtonCSV = Checkbutton(self.root, text='Creat .csv', variable=self.check)
        self.checkButtonCSV.grid(column=3, row=1)
        # Graph
        # TO DO
        self.root.mainloop()

    def applyChosenDiametre(self):
        self.labelDiametrePrint.config(text=self.entryChosenDiametre.get())

    def start_stop(self):
        if self.buttonStartStop['text'] == 'Start':
            self.buttonStartStop.config(text="Stop")
            self.startPrograme = True
            self.createCSV()
            self.traceFiber()
            self.showLenght()
            self.showWidth()
            self.showMotorSpeed()
            if self.check.get() == 1:
                self.inputCSV()
            print('start')
        elif self.buttonStartStop['text'] == 'Stop':
            self.buttonStartStop.config(text="Start")
            self.startPrograme = False
            
    def getLenght(self):
        self.lenght += 1
        return self.lenght

    def showLenght(self):
        if self.startPrograme:
            self.labelLenghtPrint.config(text=self.getLenght())
            self.labelLenghtPrint.after(self.refrechTime, self.showLenght)

    def getWidth(self):
        # coefAnalgToDiam = 1.1
        # return self.arduino.readAnalogPin(0,100,1000) * coefAnalgToDia
        self.width = random.uniform(1,10)
        self.widths.append(self.width)
        return self.width

    def showWidth(self):
        if self.startPrograme:
            self.labelWidthPrint.config(text=self.getWidth())
            self.labelWidthPrint.after(self.refrechTime, self.showWidth)

    def getMotorSpeed(self):
        pass

    def showMotorSpeed(self):
        if self.startPrograme:
            self.labelSpeedPrint.config(text=self.getMotorSpeed)
            self.labelSpeedPrint.after(self.refrechTime, self.showMotorSpeed)

    def traceFiber(self):
        self.widthCanvasValue = 4
        if self.startPrograme:
            if len(self.widths) > 0: 
                maxWidth = max(self.widths)
                if len(self.widths) <= self.canvasWidth/self.widthCanvasValue-1:
                    self.canvasFiber.delete("all")
                    for ind, val in enumerate(self.widths):
                        self.canvasFiber.create_rectangle(ind*4,(self.canvasHeight-(0.8*self.canvasHeight)/maxWidth*val)/2,ind*4+4,(self.canvasHeight+(0.8*self.canvasHeight)/maxWidth*val)/2,fill='black')
                    self.canvasFiber.after(self.refrechTime, self.traceFiber)
                if len(self.widths) > self.canvasWidth/self.widthCanvasValue-1:
                    self.widths.pop(0)
                    self.canvasFiber.delete("all")
                    for ind, val in enumerate(self.widths):
                        self.canvasFiber.create_rectangle(ind*4,(self.canvasHeight-(0.8*self.canvasHeight)/maxWidth*val)/2,ind*4+4,(self.canvasHeight+(0.8*self.canvasHeight)/maxWidth*val)/2,fill='black')
                    self.canvasFiber.after(self.refrechTime, self.traceFiber)
            else:
                if len(self.widths) <= self.canvasWidth/self.widthCanvasValue-1:
                    self.canvasFiber.delete("all")
                    for ind, val in enumerate(self.widths):
                        self.canvasFiber.create_rectangle(ind*4,(self.canvasHeight-(0.8*self.canvasHeight)*val)/2,ind*4+4,(self.canvasHeight+(0.8*self.canvasHeight)/maxWidth*val)/2,fill='black')
                    self.canvasFiber.after(self.refrechTime, self.traceFiber)
                if len(self.widths) > self.canvasWidth/self.widthCanvasValue-1:
                    self.widths.pop(0)
                    self.canvasFiber.delete("all")
                    for ind, val in enumerate(self.widths):
                        self.canvasFiber.create_rectangle(ind*4,(self.canvasHeight-(0.8*self.canvasHeight)*val)/2,ind*4+4,(self.canvasHeight+(0.8*self.canvasHeight)/maxWidth*val)/2,fill='black')
                    self.canvasFiber.after(self.refrechTime, self.traceFiber)

    def createCSV(self):
        if self.check.get() == 1:
            self.csv = CreateCSV(self.entryNameOfFile.get(),'/Users/josephgaulin/Documents/GitHub/nanocomposite-fab/Fiber_Drawing_Tower/Values')
        else:
            pass

    def inputCSV(self):
        self.csv.inputValues((self.getWidth(), self.getLenght()))
        self.checkButtonCSV.after(self.refrechTime, self.inputCSV)
        

    def update(self):
        pass



        

GUI_TourAFibre()


# index = 0


# def update():
#     global index
#     index += 1
#     lettres = ["a","b","c","d","e"]
#     lettre = lettres[index%5]
#     label.config(text=lettre)
#     label2.config(text=index)
#     # t.sleep(0.01)
#     window.after(10, update)



# window = Tk()
# window.geometry()
# #Test of the update fonction
# label = Label(window, text='Start')
# label2 = Label(window, text='Start')
# label.pack()
# label.config(text="Hello wordl!")
# label2.pack()
# my_button = Button(window, text='Start showing lettre', command=update)
# my_button.pack()

# # Apply some new text in the window
# def apply():
#     print(entry.get)
#     label3.config(text=entry.get())

# label3 = Label(window,text="Try to input texte")
# label3.pack()
# entry = Entry(window)
# entry.pack()
# # button2 = Button(window,text="show the entry", command=show(entry))
# button2 = Button(window,text="Show the entry", command=apply)
# button2.pack()

# # Create continus frame to draw the fiber
# lenght = 0
# wight = [1,2,1,2,1,2,1,2,1,2,1,2]
# def is_new_value():
#     return False

# def new_value():
#     return 0

# def draw_the_fiber(height = 0, wight = []):
#     if is_new_value():
#         wight.append(new_value())
#     canvas.create_line(height+100,0,height+100, wight[height])
#     if height < len(wight):
#         height += 1
#         draw_the_fiber(height, wight)


    
# canvas = Canvas(window)
# button4 = Button(window,text="Print the fiber", command=partial(draw_the_fiber, 0, wight))
# button4.pack()
# canvas.pack()


# window.mainloop()