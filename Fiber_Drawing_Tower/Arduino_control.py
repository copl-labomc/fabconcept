# This code is use to controle the ARDUINO wich is commanding all the systemes of the
# tower. For exemple the motors, the KEYENCE tool and the temperature controler.
import time # Using module time
# import keyboard #Using module keyboard 

# Instale pyfirmata library if it isn't already
try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util


# Start the iterator of the Arduino
board = Arduino('/dev/cu.usbmodem1101') # Work for a MAC conection change to 'COM3' for windows
it = util.Iterator(board)
it.start()

#Read the 3 output
analog_0 = board.get_pin('a:0:i')

while True:
    time.sleep(0.2)
    print(analog_0.read())