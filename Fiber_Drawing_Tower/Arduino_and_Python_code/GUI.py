import tkinter as tk
import serial
from tkinter import ttk
from time import time
from datetime import datetime
import numpy as np
from pandas import DataFrame


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
            s = serial.Serial(port)
            result.append(port)
            s.close()
        except (OSError, serial.SerialException):
            pass
    if result == []:
        return ["None"]
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
        
        """
        def __init__(self):
            """Creates the GUI, initializes the serial communication then starts the main loop
            """
            self.createGui()
            self.running = True
            self.initialization(self.current_port.get())
            self.program_loop()

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
                -Reconnect: Tries connecting to the selected port
                -Check Ports: Refreshes the available ports menu
            
            Parameters
                Text box: Type the desired diameter to send (WIP)
                Send: Send the contents of the text box to the arduino
            """

            # Create a tk application
            self.root = tk.Tk()
            self.root.title("Fiber Tower")
            self.root.geometry("500x400")
            self.root.protocol("WM_DELETE_WINDOW", self.close_window)
            
             

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
            self.spool_frame.grid(row=8, column=1, rowspan=3, columnspan=3)


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
            self.parameter_frame.grid(row=2, column=4, rowspan=3, columnspan=3, padx=5, pady=5)

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
            """
            ## Debug section
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

            #If COM4 is available, it picks it as default when lauching or else it picks the first one available
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
                self.ser.close()

        def send_diameter(self):
            """Send the desired diameter"""
            entry = self.diameter_entry.get()
            if entry != '':
                self.port_write(entry)
                #send end character
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
            """Checks if the arduino is connected then sends the command trough the serial port"""
            if self.status_label.cget("text") == "Connected":
                self.ser.write(command.encode())

        def record_diameter(self):
            if self.recording:
                self.recording = False
                self.record_button.config(text = "Record diameter", bg = "grey94")
                #Save file


                df = DataFrame(self.save_data)
                df.to_csv(f'../Drawing_data/{datetime.today().strftime("%Y%m%d, %Hh%Mm%Ss")}.csv', index=False)
            else:
                self.recording = True
                self.buffer = []
                self.save_data = {
                    "relative_time" : [],
                    "diameter" : [],
                    "preform_speed" : [],
                    "spool_speed" : []
                }
                self.start_time = time()
                self.record_button.config(text = 'Stop recording', bg = 'red')

        def check_ports(self):
            """Updates the connection drop menu with available ports"""    

            self.connection_drop_menu['menu'].delete(0, 'end')

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
                        # Only records the data when 25 elements are saved in the buffer
                        if len(self.buffer) >= 25:
                            #Convert the 2d array into a numpy array
                            treated_buffer = np.array(self.buffer)

                            #Save the time relative to the start of the recording
                            self.save_data["relative_time"].append(time() - self.start_time)
                            #Save the diameter into memory. The array is seperated, then every element is converted from a string to a float
                            #The average of the last 25 readings is saved
                            self.save_data["diameter"].append(np.mean(treated_buffer[:,2].astype(np.float16)))

                            # Same for the speed of each motor. Values are integers instead of floats
                            self.save_data["preform_speed"].append(np.mean(treated_buffer[:,0].astype(np.int16)))
                            self.save_data["spool_speed"].append(np.mean(treated_buffer[:,1].astype(np.int16)))
                            
                            # Reset the buffer
                            self.buffer = []
            except serial.SerialException:
                self.ser.close()
                self.status_label.config(text="Disconnected", bg = 'red')
                self.check_ports()
                self.reconnection_loop()

        def reconnection_loop(self): 
            """Executes a secondary loop while the program waits to be reconnected"""
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
                        if isinstance(float(recentPacketString[0]), float):
                            self.speed_preform.config(text= "Speed : " + f"{int(recentPacketString[1]):03d}")
                        if isinstance(float(recentPacketString[1]), float):
                            self.speed_spool.config(text= "Speed : " + f"{int(recentPacketString[2]):03d}")
                        if isinstance(float(recentPacketString[2]), float):
                            self.diameter.config(text= "Diameter : " + recentPacketString[3])
                        
                        # Checks that all the data has been transmitted and decoded correctly 
                        if self.recording and len(recentPacketString) == 4:
                            # Saves the data to the buffer
                            self.buffer.append(recentPacketString[:3])
                        

                        #Outputs the delay and serial packet info on the GUI (for testing)
                        #Removes the \r\n characters at the end
                        #self.serial_print.config(text = "Serial: " + "' '".join(recentPacketString))
                    except IndexError:
                        pass
                        
            # Try to avoid bad bytes
            except UnicodeDecodeError:
                pass

#Only create an instance if this program run directly
if __name__ == "__main__":
    tower = FiberTower()
