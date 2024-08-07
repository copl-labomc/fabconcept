"""
Fiber drawing tower Graphical User Interface

The code has two parts: Directly on the Arduino and on the laptop.

Here is the python code running on the laptop. The GUI itself is created with Tkinter,
a simple, esay to use graphics library. All the buttons are linked to a python function that is executed
every time the button is pressed.

This part of the code has to communicate with the Arduino. It does so using the Pyserial library.
We can send specific characters through the serial line and the Arduino can read them and react accordingly.
The python code also receives information such as motor speed and diameter from the Arduino.

See the comments in the code itself for a more detailled explanation

"""
import tkinter as tk
import serial
from tkinter import ttk
from time import time, sleep
from datetime import datetime, timedelta
import numpy as np
from pandas import DataFrame
import json

import serial.serialutil

def serial_ports():
    """ Finds all the port in use and returns it as a list. Returns ["None"] if no port is available

    Returns:
    List of all available ports
    """
    
    #Try every possible port 
    ports = ['COM%s' % (i + 1) for i in range(10)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port) #Tries opening the COM port
            result.append(port) # Adds it to a list
            s.close()
        except (OSError, serial.SerialException):
            pass #If a serial communication cannot be established, it raises the SerialException error
    if result == []:
        return ["None"] #If no port are available, the "None" string is returned (this is a quick fix that made it work). A regular None type should be better and replaced in the future
    return result



class FiberTower():
        """Object encompassing all the functions for the fiber tower's control and graphical interface.
        Automatically starts when an instance of this object is created

        Instruction dictionnary for serial communication:
        s start capstan
        a stop capstan
        t preform up
        b preform down
        k stop preform
        w start spool
        q stop spool
        r run spool in reverse
        e end character for diameter desired
        f end character for capstan/preform speed ratio
        g end character for spool/capstan speed ratio
        
        """
        def __init__(self):
            """Creates the GUI, initializes the serial communication then starts the main loop
            """
            self.load_config() # Load the configuration from the .json file
            self.createGui() # Creates the tkinter GUI
            self.running = True 
            self.initialization(self.current_port.get()) #Initializes the serial communication and sends the config info to the Arduino
            self.program_loop() #Starts the main loop

        def load_config(self):
            """Loads the contents of the config.json file into a dictionnary. If no such file is found, it creates one
            """
            try:
                with open("config.json", "r") as config:
                    self.config_data = json.load(config) #reads the content of the .json file
            except FileNotFoundError:
                #If there is no config file, create it with default values
                self.config_data = {
                    "capstan_wheel_diameter": 76.2,
                    "spool_circumeference": 820,
                    "preform_linear_speed": 0.374,
                    "preform_diameter": 19.05,
                    "microstepping": 1600,
                    "preform_length": 50
                } 
                with open("config.json", "w") as config:
                    json.dump(self.config_data, config)
                
            

        def send_config(self):
            """Sends the config data through the serial port. Each element has it's own end character.
            """
            dp2vp = str(self.config_data["preform_diameter"]**2 * self.config_data["preform_linear_speed"]) #Preform diameter^2 * Preform linear speed. Send one number instead of two.
            self.port_write(dp2vp)
            self.port_write('f')

            dc = str(self.config_data["capstan_wheel_diameter"]) #Capstan wheel diameter
            self.port_write(dc)
            self.port_write('g')

            ds = str(self.config_data["spool_circumeference"]) #Spool diameter
            self.port_write(ds)
            self.port_write('h')

            micro = str(self.config_data["microstepping"]) #Microstepping of capstan and spool
            self.port_write(micro)
            self.port_write('i')

        def createGui(self):
            """Creates the Graphical User Interface

            Buttons:

            Preform motor
                -Arrow up: Raises preform
                -Arrow down: Lowers preform
                -Stop: Stops preform motor

            Capstan motor
                -Start: Turns the capstan wheels
                -Stop: Stops the capstan wheels
            
            Spool motor
                -Start: Turns the spool and pulls the fiber
                -Stop: Stops the spool
                -Reverse: Reverses the direction of the spool

            Connection
                -Drop-down menu: Select the port to connect
                -Reconnect Tries connecting to the selected port
                -Check Ports: Refreshes the available ports menu
            
            Parameters
                -Text box: Type the desired diameter to send (WIP)
                -Send: Send the contents of the text box to the arduino
            """

            # Create a tk application
            self.root = tk.Tk()
            self.root.title("Fiber Tower")
            self.root.geometry("500x400")
            self.root.protocol("WM_DELETE_WINDOW", self.close_window) #Tells tkinter to execute the close_window function when the app is closed
            
            ## PREFORM STEPPER SECTION 

            # Frame
            self.preform_frame = tk.LabelFrame(self.root, text="Preform Motor", height=100,width=150)
            self.preform_frame.grid(row=0, column=0, rowspan=3, columnspan=3, padx=5, pady=5)

            # Buttons of preform section

            self.label_up = tk.Label(self.preform_frame, text="UP", font=("Segoe Ui", 12))
            self.label_up.grid(row=0, column=0, padx=5)
            self.button_up = ttk.Button(self.preform_frame, text=u"\u2191", command= lambda: self.port_write("t"))
            self.button_up.grid(row=0, column=1, padx=5)

            self.button_stop = tk.Button(self.preform_frame, text="Stop", command= lambda: self.port_write("k"), font=(12), bg="red", fg="white")
            self.button_stop.grid(row=1, column=1, padx=5)

            self.label_down = tk.Label(self.preform_frame, text="DOWN", font=("Segoe Ui", 12))
            self.label_down.grid(row=2, column=0, padx=5)
            self.button_down = ttk.Button(self.preform_frame, text=u"\u2193", command=lambda: self.port_write("b"))
            self.button_down.grid(row=2, column=1, padx=5)

            # Printing output speed of preform motor

            self.speed_preform = tk.Label(self.preform_frame, text="Speed :")
            self.speed_preform.grid(row=3, column=0, padx=5, columnspan=2)

            ## CAPSTAN STEPPER SECTION 
            self.capstan_frame = tk.LabelFrame(self.root, text="Capstan Motor", height=120,width=150)
            self.capstan_frame.grid(row=3, column=0, rowspan=4, columnspan=3)


            # Creation of green Start button
            self.button_start = tk.Button(self.capstan_frame, text="Start", command=lambda: self.port_write("s"), font=("Segoe Ui", 12), bg="green", fg="white")
            self.button_start.grid(row=0, column=0, padx=5)

            # Creation of red Stop button
            self.button_stop = tk.Button(self.capstan_frame, text="Stop", command=lambda: self.port_write("a"), font=("Segoe Ui", 12), bg="red", fg="white")
            self.button_stop.grid(row=0, column=1, padx=5)

            # Printing output speed of capstan

            self.speed_capstan = tk.Label(self.capstan_frame, text="Speed:")
            self.speed_capstan.grid(row=1, column=0, padx=5, columnspan=2)

            ## SPOOL STEPPER SECTION 
            self.spool_frame = tk.LabelFrame(self.root, text="Spool Motor", height=120,width=150)
            self.spool_frame.grid(row=7, column=1, rowspan=3, columnspan=3)


            # Creation of green Start button
            self.spool_start = tk.Button(self.spool_frame, text="Start", command=lambda: self.port_write("w"), font=("Segoe Ui", 12), bg="green", fg="white")
            self.spool_start.grid(row=0, column=0, padx=5)

            # Creation of red Stop button
            self.spool_stop = tk.Button(self.spool_frame, text="Stop", command=lambda: self.port_write("q"), font=("Segoe Ui", 12), bg="red", fg="white")
            self.spool_stop.grid(row=0, column=1, padx=5)

            # Creation of yellow Reverse button
            self.spool_stop = tk.Button(self.spool_frame, text="Reverse", command=lambda: self.port_write("r"), font=("Segoe Ui", 12), bg="yellow", fg="black")
            self.spool_stop.grid(row=0, column=2, padx=5)

            # Printing output speed of capstan

            self.speed_spool = tk.Label(self.spool_frame, text="Speed:")
            self.speed_spool.grid(row=1, column=0, padx=5, columnspan=2)

            ## Parameter frame section 
            self.parameter_frame = tk.LabelFrame(self.root, text="Parameters", height=100,width=150)
            self.parameter_frame.grid(row=2, column=4, rowspan=7, columnspan=3, padx=5, pady=5)

            # printing diameter measured by laser sensor
            self.diameter = tk.Label(self.parameter_frame, text="Diameter: 0.00")
            self.diameter.grid(row=0, column=0, padx=5)

            # input for the diameter desired
            self.diameter_desired = tk.Label(self.parameter_frame, text='Diameter desired :')
            self.diameter_desired.grid(row=1, column=0)
            self.diameter_entry = tk.Entry(self.parameter_frame)
            self.diameter_entry.grid(row=1, column=1)
            self.diameter_entry_button = tk.Button(self.parameter_frame, text = 'Send', command=self.send_diameter)
            self.diameter_entry_button.grid(row=1, column = 2)


            #Record diameter button
            self.record_button = tk.Button(self.parameter_frame, text = "Record diameter", command=self.record_diameter)
            self.record_button.grid(row=0, column=1)
            self.recording = False

            #time elapsed
            self.time_elapsed = tk.Label(self.parameter_frame, text="Time elapsed: ")
            self.time_elapsed.grid(row=2, column=0)

            #length drawn
            self.length_drawn = tk.Label(self.parameter_frame, text="Length drawn: ")
            self.length_drawn.grid(row=3, column=0)

            self.progress = tk.Label(self.parameter_frame, text="Progress: ")
            self.progress.grid(row=4, column=0)

            self.time_remaining = tk.Label(self.parameter_frame, text="Time remaining: ")
            self.time_remaining.grid(row=5, column=0)
            
            """
            
            ## Debug section
            # This debug section can be added back in for development. It just prints the contents of the recived serial info directly on the GUI.
            #Debug screen with time delay and received serial packets
            self.debug_frame = tk.LabelFrame(self.root, text="Debug", height=100,width=150)
            self.debug_frame.grid(row=5, column=4, rowspan=2, columnspan=3, padx=5, pady=5)
            self.serial_print = tk.Label(self.debug_frame, text="Serial")
            self.serial_print.grid(row=1, column=3, padx=5, columnspan= 3)"""


            ##Connection frame section
            self.connection_frame = tk.LabelFrame(self.root, text="Connection", height=50,width=150)
            self.connection_frame.grid(row=0, column=4, rowspan=2, columnspan=2, padx=5, pady=5)

            # Port selection menu

            self.connect_button = tk.Button(self.connection_frame, text = "Reconnect", command=self.reconnect)
            self.connect_button.grid(row=0, column=1 , padx=5)

            self.connect_button = tk.Button(self.connection_frame, text = "Check Ports", command=self.check_ports)
            self.connect_button.grid(row=1, column=1 , padx=5)

            self.status_label = tk.Label(self.connection_frame, text = "Status: Disconnected", bg = 'red')
            self.status_label.grid(row=1, column=0 , padx=5)

            self.current_port = tk.StringVar()

            ### Start/Stop all buttons
            self.stop_all_frame = tk.LabelFrame(self.root, text= "All")
            self.stop_all_frame.grid(row=11,column=0, columnspan=3)

            self.stop_all_button = tk.Button(self.stop_all_frame, text = "Stop", bg = "red", font=("Segoe Ui", 12), fg="white", command=lambda: self.port_write("akq"))
            self.stop_all_button.grid(column=1, row=0)


            self.start_all_button = tk.Button(self.stop_all_frame, text = "Start", bg = "green", font=("Segoe Ui", 12), fg="white", command=lambda: self.port_write("sbw"))
            self.start_all_button.grid(column=0, row=0)


            #If COM4 is available, it picks it as default when lauching or else it picks the first one available
            #COM4 is usually the port used by the lab's laptop. For some reason, a COM3 port also exists. I have no idea where it comes form but it just spits back what you send it. This breaks the code
            if "COM4" in serial_ports():
                self.current_port.set("COM4") 
            else:
                self.current_port.set(serial_ports()[0]) 

            self.connection_drop_menu = tk.OptionMenu(self.connection_frame, self.current_port, *serial_ports())
            self.connection_drop_menu.grid(row=0, column=0,columnspan=1, padx=5)

        def close_window(self):
            """Close serial communication when the window is closed"""
            self.running = False  # turn off while loop
            if self.status_label.cget('text') == "Connected":
                # Only close the serial port if it is open in the first place
                self.ser.close()

        def send_diameter(self):
            """Send the desired diameter"""
            entry = self.diameter_entry.get()
            if entry != '':
                self.port_write(entry)
                self.port_write('e')

        def reconnect(self):
            """Tries to reconnect to the arduino when the Reconnect button is pressed"""
            try:
                self.initialization(self.current_port.get())
                self.program_loop()
            except IndexError:
                self.status_label.config(text = "No Available Port", bg = 'yellow')
            except serial.serialutil.SerialException:
                #Triggers when connection is already established with the same port
                pass
        
        def port_write(self, command):
            """Checks if the arduino is connected then sends the command trough the serial port.
            The ser.write function sends the string one character at a time so and ending character needs to be sent to let the arduino know that the message is done"""
            if self.status_label.cget("text") == "Connected":
                self.ser.write(command.encode())

        def record_diameter(self):
            """If not already recording, start the recording. If recording, save it as a .csv file.
            """
            if self.recording:
                self.recording = False
                self.record_button.config(text = "Record diameter", bg = "grey94")

                #Save file

                df = DataFrame(self.save_data) #The pandas library is used to save the diameter data
                df.to_csv(f'../Drawing_data/{datetime.today().strftime("%Y%m%d, %Hh%Mm%Ss")}.csv', index=False)
            else:
                self.recording = True
                self.buffer = []
                self.save_data = {
                    "relative_time" : [],
                    "diameter" : [],
                    "preform_speed" : [],
                    "spool_speed" : [],
                    "capstan_speed" : []
                }
                self.start_time = time()
                self.record_button.config(text = 'Stop recording', bg = 'red')
                self.length_drawn_value = 0
                self.drawn_volume = 0
                self.preform_volume = self.config_data["preform_diameter"]**2 * np.pi * self.config_data["preform_length"]

        def check_ports(self):
            """Updates the connection drop menu with available ports"""    

            self.connection_drop_menu['menu'].delete(0, 'end') #I found no way to modify the menu options so the menu is deleted and a new one is created

            ports = serial_ports()
            if self.status_label.cget('text') == "Connected":
                #If the serial port is already in use, it will not be detected and needs to be added manually to the list
                if ports[0] == "None":
                    ports = [self.current_port.get()]
                else:
                    ports.insert(0,self.current_port.get())

            #Creates a new instance of the menu with the updated ports
            self.current_port.set(ports[0])
            for port in ports:
                self.connection_drop_menu['menu'].add_command(label=port, command=tk._setit(self.current_port, port))

        def initialization(self, commPort):
            """Initializes the serial communication. If no comm port is available, sends the tower in the reconnection loop 
            """
            if commPort == "None":
                self.status_label.config(text="No Available Port", bg = 'yellow')
                self.reconnection_loop()
            else:
                self.ser = serial.Serial(commPort, baudrate = 115200, timeout = 1)
                self.status_label.config(text="Connected", bg = 'green')
                sleep(2) #Waits that the serial connection is well established before sending the config
                self.send_config()

        #Loop functions

        def program_loop(self):
            """Executes the main program loop when called"""
            try:
                while True:
                    self.root.update()
                    if not self.running: 
                        break
                    self.checkSerialPort()
                    if self.recording:
                        # Only records the data when 5 elements are saved in the buffer
                        if len(self.buffer) >= 5:
                            #Convert the 2d array into a numpy array
                            treated_buffer = np.array(self.buffer)

                            #Save the diameter into memory. The array is seperated, then every element is converted from a string to a float
                            #The average of the last 5 readings is saved
                            self.save_data["diameter"].append(np.mean(treated_buffer[:,3].astype(np.float16)))

                            # Same for the speed of each motor. Values are integers instead of floats
                            self.save_data["preform_speed"].append(np.mean(treated_buffer[:,1].astype(np.int16)))
                            self.save_data["spool_speed"].append(np.mean(treated_buffer[:,2].astype(np.int16)))
                            self.save_data["capstan_speed"].append(np.mean(treated_buffer[:,0].astype(np.int16)))

                            #Save the time relative to the start of the recording
                            elapsed = time() - self.start_time

                            #Doesn't do anything on first loop
                            if len(self.save_data["relative_time"]) >= 1:
                                #calculates time difference
                                time_delta = elapsed - self.save_data["relative_time"][-1]
                                #calculates length difference
                                length_delta = time_delta*np.pi * self.config_data["capstan_wheel_diameter"] * self.capstan_speed_value / self.config_data["microstepping"] / 5 # 5 is the motor gear ratio
                                #calculates fiber volume difference
                                volume_delta = float(self.save_data['diameter'][-1])**2 * length_delta
                                #adds the volume difference to the total
                                self.drawn_volume += volume_delta
                                #calculates volume of fiber yet to be drawn
                                remaining_volume = self.preform_volume - self.drawn_volume
                                #calculate progress %
                                progress = 1- remaining_volume / self.preform_volume
                                self.progress.config(text = f"Progress: {round(progress * 100, 2)}%")
                                #estimates remaining time. the small number is to avoid division by 0
                                time_remaining = elapsed / (progress + 0.000000001) - elapsed

                                #checks that the estimation is reasonable i.e. within a day 
                                if time_remaining < 86400:
                                    self.time_remaining.config(text = f"Time remaining: {str(timedelta(seconds=round(time_remaining)))}")
                            else:
                                #makes the length difference 0 on the first loop 
                                length_delta = 0


                            self.save_data["relative_time"].append(elapsed)
                            self.time_elapsed.config(text=f"Time elapsed: {str(timedelta(seconds=int(elapsed)))}")

                            #modifies the total drawn length incrementally
                            self.length_drawn_value += length_delta
                            self.length_drawn.config(text=f"Length drawn: {round(self.length_drawn_value / 1000, 2)} m") 
                            
                            # Reset the buffer
                            self.buffer = []

            except serial.SerialException:
                #If something goes wrong with the serial connection, 
                self.ser.close() #close the port
                self.status_label.config(text="Disconnected", bg = 'red')
                self.check_ports() #Check the available ports
                self.reconnection_loop() #Go to the idle state

        def reconnection_loop(self): 
            """Executes a secondary loop while the program waits to be reconnected. Only updates the GUI and doesn't check the serial port"""
            while True:
                self.root.update()
                if not self.running: 
                    break
        
        def checkSerialPort(self):
            """Check serial input from the arduino and put the value back into the corresponding label. 
            String arriving from the arduino has the format "value1, value2, etc"
            """
            try: 
                # if serial communication is open and data is waiting in arduino
                if self.ser.isOpen() and self.ser.in_waiting:
                    # Read the output line of the arduino and make a list of each element
                    recentPacket = self.ser.readline()
                    #Decodes the packet, then removes the ending \r\n characters and finally separates the different values
                    recentPacketString = recentPacket.decode('utf').replace("\r\n", "").split(",")
                    # Update the value for each printed values if its a float (can be an altered value)
                    try:
                        if isinstance(float(recentPacketString[0]), float):
                            self.speed_capstan.config(text= "Speed : " + f"{int(recentPacketString[0]):03d}")
                            self.capstan_speed_value = int(recentPacketString[0])
                        if isinstance(float(recentPacketString[1]), float):
                            self.speed_preform.config(text= "Speed : " + f"{int(recentPacketString[1]):03d}")
                        if isinstance(float(recentPacketString[2]), float):
                            self.speed_spool.config(text= "Speed : " + f"{int(recentPacketString[2]):03d}")
                        if isinstance(float(recentPacketString[3]), float):
                            self.diameter.config(text= "Diameter : " + recentPacketString[3])
                        # Checks that all the data has been transmitted and decoded correctly 
                        if self.recording and len(recentPacketString) == 4:
                            # Saves the data to the buffer
                            self.buffer.append(recentPacketString[:4])
                    except IndexError:
                        pass   
            # Try to avoid bad bytes
            except UnicodeDecodeError:
                pass

#Only create an instance if this program run directly
if __name__ == "__main__":
    tower = FiberTower()
