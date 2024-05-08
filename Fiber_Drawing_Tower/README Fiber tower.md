# Instruction manual for the FIber Drawing Tower #

## Hardware ##

## GUI ##

The graphical user interface is run from the connected computer's executable gui.py file. It is developped using the tkinter library.

The buttons under "Preform Motor" controls, as the name implies, the top motor that adjusts the furnace height. The top and bottom arrows lift the furnace up and down while the Stop button makes it stop moving.

The "Cabestan Motor" section constrols the cabestan. It can be turned on or off with the buttons.

The speed of both motors can be adjuted with potentiometer, currently on the breadboard. Motor speed is diplayed in each of the two former sections.

## Backend software ##

The computer running the python GUI code communicates with the arduino board with byte string messages, the pyserial python library. The letters s, a, t, b, and k are sent to start and stop the cabestan as well as to move up, move down and stop the preform motor. 

The system also receives information from the laser diameter sensor. This analog signal is converted to the real diameter measurement in code. 