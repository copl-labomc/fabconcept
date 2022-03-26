# This code is use to controle the ARDUINO wich is commanding all the systemes of the
# tower. For exemple the motors, the KEYENCE tool and the temperature controler.
from optparse import Values
import time
from unicodedata import name
from matplotlib.pyplot import uninstall_repl_displayhook
import pandas as pd
import csv
from datetime import date

from sklearn.preprocessing import Binarizer
# Instale pyfirmata library if it isn't already
class Control:
    def __init__(self, COM: str):
        try:
            from pyfirmata import Arduino, util
        except:
            import pip
            pip.main(['install','pyfirmata'])
            from pyfirmata import Arduino, util
        self.COM = COM
        self.board = Arduino(COM)
        self.it = util.Iterator(self.board)
        self.it.start()

    def readAnalogPin(self, num: int, frequency: int, until=True):
        self.pin = self.board.get_pin('a:' + str(num) + ':i')
        if until:
            while until:
                value = self.pin.read()
                time.sleep(1/frequency)
                try:
                    print(value)
                except TypeError:
                    continue
                return self.pin.read()
        else:
            iteration = -1
            while iteration <= until:
                iteration += 1
                value = self.pin.read()
                time.sleep(1/frequency)
                try:
                    print(value)
                except TypeError:
                    continue
                return self.pin.read()

    def readDigitalPin(self, num: int, frequency: int, until=True):
        self.pin = self.board.get_pin('d:' + str(num) + ':i')
        return self.pin.read()
        if until:
            while until:
                value = self.pin.read()
                time.sleep(1/frequency)
                try:
                    print(value)
                except TypeError:
                    continue
                return self.pin.read()
        else:
            iteration = -1
            while iteration <= until:
                iteration += 1
                value = self.pin.read()
                time.sleep(1/frequency)
                try:
                    print(value)
                except TypeError:
                    continue
                return self.pin.read()

    def outputAnalogPin(self, num: int, val: float):
        self.pin = self.board.get_pin('d:' + str(num) + ':p')
        return self.pin.write(val)

    def outputDigitalPin(self, num: int):
        self.pin = self.board.get_pin('d:' + str(num) + ':o')
        return self.pin.wright(1)

    
class CreateCSV:
    def __init__(self, name: str, path: str):
        try:
            import csv
        except:
            import pip
            pip.main(['install','csv'])
            import csv
        self.name = name
        self.path = path
        self.today = str(date.today())
        self.time = time.time()
        open(name + '_' + self.today +'.csv','a').close()
        self.values = []

    def inputValues(self, value: tuple):
        self.values.append(value)
        if len(self.values) >= 100:
            with open(self.name + '_' + self.today + '.csv', 'a') as file:
                csv.writer(file).writerows(self.values)
            self.values = []





# val = CreateCSV('S','/Users/josephgaulin/Documents/GitHub/nanocomposite-fab/Fiber_Drawing_Tower/Values')
# # a = Control('/dev/cu.usbmodem2101')
# for i in range(10000):
#     val.inputValues((i, i+1)) 

# # Create a CSV file (y/n)
# print('Do you want to put your value in a file?   (y/n)')
# in_file = input()
# if in_file == "y":
# #Creating a file
#     print('What name do you want to asign to your file?')
#     file_name = input()
#     # Time of the aquisition
#     today = str(date.today())
#     print('Your file name is ' + file_name + '_' + today + '\nThe aquisition is running...')
# # Wright a file and move it in GitHub
#     with open(file_name + '_' + today +'.csv','a') as f:
#         csv_writer = writer(f)
#         csv_writer.writerow(values)
# # Modifier l'endroit le ficher et envoyer selon l'ordinateur
#     shutil.move(file_name + '_' + today + '.csv', '/Users/josephgaulin/Documents/GitHub/nanocomposite-fab/Fiber_Drawing_Tower/Values')
#     print('Aquisition done')
# if in_file == "n":    
#     print("Hear's the values:")
#     print(values)


# # Begin the iterator of the Arduino
# board = Arduino('/dev/cu.usbmodem2101') # Work for a MAC conection change to 'COM3' for windows  cu.usbmodem1101
# it = util.Iterator(board)
# it.start()

# ### Setting of the Arduino ###
# # Normal setting (reading A0)
# pin = board.analog[0]
# pin.enable_reporting()
# #Change de pin input
# print('Do you want to use a dierent pin then the A0 to read the input?(y/n)')
# pin_yn = input()
# if pin_yn == 'y':
#     print('What\'s the number of the pin?')
#     pin = input()
# # Frequence of accuisition set at 100Hz
# frequency = 100
# print('Do you want to use a dierent frequency then the 100Hz to read the input?(y/n)')
# if pin_yn == 'y':
#     print('What frequency do you want?')
#     frequency = input()
#     print("aquisition strat")
# else:
#     print("aquisition start")

# # Read the A0 input and put it in a csv file
# time.sleep(1)
# go = True
# values = []
# while go:
#     value = float(pin.read())*5
#     time.sleep(1/frequency)
#     values += [str(value)]
#     if len(values) == 1000:
#         go = False

