# Instruction manual for the FIber Drawing Tower #

## Hardware ##

The two stepper motors are controlled with a M415B driver each. The brain of the the tower is an Arduino Uno connected to a laptop computer running a python script and displaying the GUI. The motors and furnace are powered with the Keyence CA-U4 24 V power supply. 

## GUI ##

The graphical user interface is run from the connected computer's executable gui.py file. It is developed using the tkinter library.

The buttons under "Preform Motor" controls, as the name implies, the top motor that adjusts the furnace height. The top and bottom arrows lift the furnace up and down while the Stop button makes it stop moving.

The "Cabestan Motor" section controls the cabestan. It can be turned on or off with the buttons.

The speed of both motors can be adjusted with potentiometer, currently on the breadboard. Motor speed is displayed in each of the two former sections.

## Backend software ##

The computer running the python GUI code communicates with the Arduino board with byte string messages, the pyserial python library. The letters s, a, t, b, and k are sent to start and stop the cabestan as well as to move up, move down and stop the preform motor. 

The system also receives information from the laser diameter sensor. This analog signal is converted to the real diameter measurement in code. 

## Known bugs ##

The GUI and the Arduino are running independently. The Arduino will sometimes think it is still connected from a previous use and the GUI will not open properly. An error message appears on screen. Simply disconnect and reconnect the Arduino to the computer.

If the system crashes, the only way to start it back up again is to restart the computer. One way to make it crash is to turn down a potentiometer to zero, which creates a short circuit. Resistor should be added in the near future.