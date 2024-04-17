import pyfirmata
import time

v = 0.1

board = pyfirmata.Arduino('/dev/cu.usbmodem1101')

it = pyfirmata.util.Iterator(board)
it.start()

speed = board.get_pin('d:9:p')
diametre = board.get_pin('a:0:r')

while True:
    v = diametre.read()
    speed.write(v)
    print(v)
    time.sleep(0.1)

