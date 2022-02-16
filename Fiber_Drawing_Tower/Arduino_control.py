# This code is use to controle the ARDUINO wich is commanding all the systemes of the
# tower. For exemple the motors, the KEYENCE tool and the temperature controler.
import time # Using module time
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
# Instale keyboard library if it isn't already
try:
    import keyboard
except:
    import pip
    pip.main(['install','keyboard'])
    import keyboard

# Time of the aquisition
today = str(date.today())
# Start the iterator of the Arduino
board = Arduino('/dev/cu.usbmodem1101') # Work for a MAC conection change to 'COM3' for windows  cu.usbmodem1101
it = util.Iterator(board)
it.start()

# Normal setting (reading A0)
A0 = board.analog[0]
A0.enable_reporting()

# Create a CSV file 
print('What name do you want to asign to your file?')
file_name = input()
print('Your file name is ' + file_name + '_' + today + '\nThe aquisition is running...')

# Read the A0 input and put it in a csv file
time.sleep(1)
go = True
values = []
while go:
    value = float(A0.read())*5
    time.sleep(0.01)
    values += [str(value)]
    if len(values) == 1000:
        go = False

# Wright a file and move it in GitHub
with open(file_name + '_' + today +'.csv','a') as f:
    csv_writer = writer(f)
    csv_writer.writerow(values)
# Modifier l'endroit le ficher et envoyer selon l'ordinateur
shutil.move(file_name + '_' + today + '.csv', '/Users/josephgaulin/Documents/GitHub/nanocomposite-fab/Fiber_Drawing_Tower/Values')
print('Aquisition done')