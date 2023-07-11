from tkinter import *
import random
import numpy as np
import time
from simple_pid import PID
import pyfirmata


class GUI_TourAFibre:
    def __init__(self, com_port):
        '''
        Cette class produit une interface utilisateur pour comander la tour à fibre
        - com_port : port de communication de l'Arduino
        '''
        # Initialisation de la carte Arduino
        self.board = pyfirmata.Arduino(com_port)
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.speedTension = self.board.get_pin('d:9:p')
        self.diametre = self.board.get_pin('a:0:r')
        #Simulation du diamètre de la fibre
        self.sim = DrawingSimulation(100,20,0.01)
        self.fiber_speed = 10
        self.dt = 0.1

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
        self.labelSpeedUnit = Label(self.root, text='mm/s')
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
        self.labelTension = Label(self.root, text='Tension:')
        self.labelTension.grid(column=4,row=6)
        self.labelTensionPrint = Label(self.root, text='None')
        self.labelTensionPrint.grid(column=5, row=6, )
        self.labelTensionUnit = Label(self.root, text='V')
        self.labelTensionUnit.grid(column=6,row=6)
        self.labelNameOfFile = Label(self.root, text='File name:')
        self.labelNameOfFile.grid(column=4, row=1)
        self.labelNameOfFileType = Label(self.root, text='.csv')
        self.labelNameOfFileType.grid(column=6, row=1)
        # Buttons
        self.buttonDiametre = Button(self.root, text='Apply', command=self.applyChosenDiametre)
        self.buttonDiametre.grid(column=2, row=3)
        self.buttonStartStop = Button(self.root, text='Start', command=self.start_stop)
        self.buttonStartStop.grid(column=4, row=7)
        # Canvas
        self.canvasHeight = 100
        self.canvasWidth = 400
        self.canvasFiber = Canvas(self.root, bg='grey', height=self.canvasHeight, width=self.canvasWidth)
        self.canvasFiber.grid(column=0, row=7)
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
            # GUI
            self.buttonStartStop.config(text="Stop")
            self.startPrograme = True
            self.createCSV()
            self.traceFiber()
            self.showTension()
            self.showLenght()
            self.showWidth()
            self.showMotorSpeed()
            if self.check.get() == 1:
                self.inputCSV()
            print('start')
        elif self.buttonStartStop['text'] == 'Stop':
            # Arduino
            self.speedTension.write(0)
            self.buttonStartStop.config(text="Start")
            self.startPrograme = False
            
    def getTension(self):
        speed = self.getMotorSpeed()
        print(speed)
        return speed/11.5
    
    def showTension(self):
        if self.startPrograme:
            self.speedTension.write(self.getTension())
            self.labelTensionPrint.config(text=self.getTension())
            self.labelTensionPrint.after(self.refrechTime, self.showTension)
        else:
            self.speedTension.write(0)
            self.labelTensionPrint.config(text=0)
            self.labelTensionPrint.after(self.refrechTime, self.showTension)
    
    def getLenght(self):
        self.lenght += (self.fiber_speed*self.dt)/1000
        return round(self.lenght,3)

    def showLenght(self):
        if self.startPrograme:
            self.labelLenghtPrint.config(text=self.getLenght())
            self.labelLenghtPrint.after(self.refrechTime, self.showLenght)

    def getWidth(self):
        # coefAnalgToDiam = 1.1
        # return self.arduino.readAnalogPin(0,100,1000) * coefAnalgToDia
        self.fiber_speed, f_d, f_pid = self.sim.one_iteration(self.dt,float(self.labelDiametrePrint['text']),self.fiber_speed,0.5,0,0)
        self.width = f_d
        self.widths.append(self.width)
        return self.width

    def showWidth(self):
        if self.startPrograme:
            self.labelWidthPrint.config(text=self.getWidth())
            self.labelWidthPrint.after(self.refrechTime, self.showWidth)

    def getMotorSpeed(self):
        speed = round(self.fiber_speed,3)
        if speed >= 11.5:
            speed = 11.5
        return speed

    def showMotorSpeed(self):
        if self.startPrograme:
            self.labelSpeedPrint.config(text=self.getMotorSpeed())
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



class DrawingSimulation:
    def __init__(self, perform_length:int, preform_diameter:int, feed_speed:int):
        '''
        Les unités de chacune des variable son les suivante:
        - prefome_length [mm]
        - preform_diameter [mm]
        - feed_speed [mm/s]
        '''
        self.premform_length = perform_length
        self.preform_diameter = preform_diameter
        self.feed_speed = feed_speed
        

    def drawing_diameter(self, speed:int):
        '''
        Les unités de chacune des variable sont les suivante:
        - speed [mm/s]
        '''
        volume_in = self.feed_speed*np.pi*(self.preform_diameter/2)**2
        fiber_diameter =  np.sqrt(volume_in/(speed*np.pi/4)) #retourne le diamètre de la fibre
        return fiber_diameter

    def one_iteration(self, dt:float, fix_diametre:float, fiber_speed:float, Kp:float, Ki:float, Kd:float):
        '''
        Les unités de chacune des variable sont les suivante
        - dt [s]
        - fix_diametre [mm]
        - fiber_speed [mm/s]
        '''
        pid = PID(Kp, Ki, Kd, fix_diametre)
        time.sleep(0.011)
        fiber_speed = fiber_speed -(pid(self.drawing_diameter(fiber_speed))/dt)
        self.premform_length -= dt*self.feed_speed
        return (fiber_speed, self.drawing_diameter(fiber_speed),pid(self.drawing_diameter(fiber_speed)))


    def simulat(self, dt:float, fix_diametre:float, fiber_speed:float, Kp:float, Ki:float, Kd:float, iteration:int):
        '''
        Les unités de chacune des variable sont les suivante
        - dt [s]
        - fix_diametre [mm]
        - fiber_speed [mm/s]
        '''
        ts = []
        t = 0
        fiber_diameter = []
        self.fix_diametre = fix_diametre
        pid = PID(Kp, Ki, Kd, fix_diametre)
        pids = []
        n = 0
        while (self.premform_length > 0 and n < iteration):
            time.sleep(0.011)
            fiber_diameter.append(self.drawing_diameter(fiber_speed))
            pids.append(pid(self.drawing_diameter(fiber_speed)))
            ts.append(t)
            fiber_speed = fiber_speed-(pid(self.drawing_diameter(fiber_speed))/dt)
            self.premform_length -= dt*self.feed_speed
            n += 1
            t += dt
        return [fiber_diameter, pids, ts]
 

GUI_TourAFibre('/dev/cu.usbmodem1101')


