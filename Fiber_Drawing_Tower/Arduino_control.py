# This code is use to controle the ARDUINO wich is commanding all the systemes of the
# tower. For exemple the motors, the KEYENCE tool and the temperature controler.
import time
from tkinter import N # Using module time
import pandas as pd
import shutil
from csv import writer
from datetime import date
# Instale pyfirmata library if it isn't already
try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util


class Control:
    def __init__(self, COM: str):
        self.COM = COM
        self.board = Arduino(COM)
        self.it = util.Iterator(self.board)
        self.it.start()
    def readPinAnalog(self, num: int):
        self.pin = self.board.analog[num]
        self.pin.enable_reporting()
        return self.pin.read()
    def readPinDigital(self, num: int):
        self.pin = self.board.digital[num]
        self.pin.enable_reporting()
        return self.pin.read()
        

# Begin the iterator of the Arduino
board = Arduino('/dev/cu.usbmodem1101') # Work for a MAC conection change to 'COM3' for windows  cu.usbmodem1101
it = util.Iterator(board)
it.start()

### Setting of the Arduino ###
# Normal setting (reading A0)
pin = board.analog[0]
pin.enable_reporting()
#Change de pin input
print('Do you want to use a dierent pin then the A0 to read the input?(y/n)')
pin_yn = input()
if pin_yn == 'y':
    print('What\'s the number of the pin?')
    pin = input()
# Frequence of accuisition set at 100Hz
frequency = 100
print('Do you want to use a dierent frequency then the 100Hz to read the input?(y/n)')
if pin_yn == 'y':
    print('What frequency do you want?')
    frequency = input()

# Read the A0 input and put it in a csv file
time.sleep(1)
go = True
values = []
while go:
    value = float(pin.read())*5
    time.sleep(1/frequency)
    values += [str(value)]
    if len(values) == 1000:
        go = False

# Create a CSV file (y/n)
print('Do you want to put your value in a file?   (y/n)')
in_file = input()
if in_file == "y":
#Creating a file
    print('What name do you want to asign to your file?')
    file_name = input()
    # Time of the aquisition
    today = str(date.today())
    print('Your file name is ' + file_name + '_' + today + '\nThe aquisition is running...')
# Wright a file and move it in GitHub
    with open(file_name + '_' + today +'.csv','a') as f:
        csv_writer = writer(f)
        csv_writer.writerow(values)
# Modifier l'endroit le ficher et envoyer selon l'ordinateur
    shutil.move(file_name + '_' + today + '.csv', '/Users/josephgaulin/Documents/GitHub/nanocomposite-fab/Fiber_Drawing_Tower/Values')
    print('Aquisition done')
if in_file == "n":    
    print("Hear's the values:")
    print(values)
