import tkinter as tk
import serial
from tkinter import ttk
import serial


def serial_ports():
    """ Finds all the port in use and returns it as a list
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

## Button functions

def close_window():
  """Close serial communication when the windows is closed"""
  global running
  running = False  # turn off while loop
  if status_label.cget('text') == "Connected":
    ser.close()


# Preform Button functions
def preform_up():
    port_write(b't')

def preform_down():
    port_write(b'b')

def stop_preform():
    port_write(b'k')

# Capstan Button functions
def start_capstan():
    """send "s" in byte to  start capstan motor
    """
    port_write(b's')

def stop_capstan():
    """send "a" in byte to stop capstan motor
    """
    port_write(b'a')

# Spool Button functions

def start_spool():
    """send "w" in byte to  start capstan motor
    """
    port_write(b'w')

def stop_spool():
    """send "q" in byte to stop spool motor
    """
    port_write(b'q')

def reverse_spool():
    """send "r" in byte to reverse spool motor
    """
    port_write(b'r')

def send_diameter():
    """ send the desired diameter"""
    entry = diameter_entry.get()
    if entry != '':
        port_write(entry.encode())
        #send end character
        port_write(b'e')

def reconnect():
    """Tries to reconnect to the arduino when the Reconnect button is pressed"""
    try:
        initialise(current_port.get())
        program_loop()
    except IndexError:
        status_label.config(text = "No Available Port", bg = 'yellow')
    except serial.serialutil.SerialException:
        #Triggers when connection is already established with the same port
        pass
 
def check_ports():
    """Updates the connection drop menu with available ports"""    

    connection_drop_menu['menu'].delete(0, 'end')

    ports = serial_ports()
    if status_label.cget('text') == "Connected":
        #If the serial port is already in use, it will not be detected and needs to be added manually to the list
        if ports[0] == "None":
            ports = [current_port.get()]
        else:
            ports.insert(0,current_port.get())

    #Creates a new instance of the menu with the updated ports
    current_port.set(ports[0])
    for port in ports:
        connection_drop_menu['menu'].add_command(label=port, command=tk._setit(current_port, port))

def port_write(command):
    """Checks if the arduino is connected then sends the command trough the serial port"""
    if status_label.cget("text") == "Connected":
        ser.write(command)

#Loop functions

def program_loop():
    """Executes the main program loop when called"""
    try:
        while True:
            root.update()
            if not running: 
                break
            checkSerialPort()
    except serial.serialutil.SerialException:
        ser.close()
        status_label.config(text="Disconnected", bg = 'red')
        check_ports()
        reconnection_loop()

def reconnection_loop(): 
    """Executes a secondary loop while the program waits to be reconnected"""
    while True:
        root.update()
        if not running: 
            break

### GUI

# Create a tk application 

root = tk.Tk()
root.title("Fiber Tower")
root.geometry("500x400")
root.protocol("WM_DELETE_WINDOW", close_window)


## PREFORM STEPPER SECTION 

# Frame
preform_frame = tk.LabelFrame(root, text="Preform Motor", height=100,width=150)
preform_frame.grid(row=0, column=0, rowspan=3, columnspan=3, padx=5, pady=5)

# Buttons of preform section

label_up = tk.Label(preform_frame, text="UP", font=("Segoe Ui", 12))
label_up.grid(row=0, column=0, padx=5)
button_up = ttk.Button(preform_frame, text=u"\u2191", command=preform_up)
button_up.grid(row=0, column=1, padx=5)

button_stop = tk.Button(preform_frame, text="Stop", command=stop_preform, font=(12), bg="red", fg="white")
button_stop.grid(row=1, column=1, padx=5)

label_down = tk.Label(preform_frame, text="DOWN", font=("Segoe Ui", 12))
label_down.grid(row=2, column=0, padx=5)
button_down = ttk.Button(preform_frame, text=u"\u2193", command=preform_down)
button_down.grid(row=2, column=1, padx=5)

# Printing output speed of preform motor

speed_preform = tk.Label(preform_frame, text="Speed :")
speed_preform.grid(row=3, column=0, padx=5, columnspan=2)


## CAPSTAN STEPPER SECTION 
capstan_frame = tk.LabelFrame(root, text="Capstan Motor", height=120,width=150)
capstan_frame.grid(row=4, column=0, rowspan=4, columnspan=3)


# Creation of green Start button
button_start = tk.Button(capstan_frame, text="Start", command=start_capstan, font=("Segoe Ui", 12), bg="green", fg="white")
button_start.grid(row=0, column=0, padx=5)

# Creation of red Stop button
button_stop = tk.Button(capstan_frame, text="Stop", command=stop_capstan, font=("Segoe Ui", 12), bg="red", fg="white")
button_stop.grid(row=0, column=1, padx=5)

# Printing output speed of capstan

speed_capstan = tk.Label(capstan_frame, text="Speed:")
speed_capstan.grid(row=1, column=0, padx=5, columnspan=2)

## SPOOL STEPPER SECTION 
spool_frame = tk.LabelFrame(root, text="Spool Motor", height=120,width=150)
spool_frame.grid(row=8, column=1, rowspan=3, columnspan=3)


# Creation of green Start button
spool_start = tk.Button(spool_frame, text="Start", command=start_spool, font=("Segoe Ui", 12), bg="green", fg="white")
spool_start.grid(row=0, column=0, padx=5)

# Creation of red Stop button
spool_stop = tk.Button(spool_frame, text="Stop", command=stop_spool, font=("Segoe Ui", 12), bg="red", fg="white")
spool_stop.grid(row=0, column=1, padx=5)

# Creation of yellow Reverse button
spool_stop = tk.Button(spool_frame, text="Reverse", command=reverse_spool, font=("Segoe Ui", 12), bg="yellow", fg="black")
spool_stop.grid(row=0, column=2, padx=5)

# Printing output speed of capstan

speed_spool = tk.Label(spool_frame, text="Speed:")
speed_spool.grid(row=1, column=0, padx=5, columnspan=2)

## Parameter frame section 
parameter_frame = tk.LabelFrame(root, text="Parameters", height=100,width=150)
parameter_frame.grid(row=2, column=4, rowspan=3, columnspan=3, padx=5, pady=5)

# printing diameter measured by laser sensor
diameter = tk.Label(parameter_frame, text="Diameter Measurement:")
diameter.grid(row=0, column=0,columnspan=4, padx=5)

# input for the diameter desired
diameter_desired = tk.Label(parameter_frame, text='Diameter desired :')
diameter_desired.grid(row=1, column=0)
diameter_entry = tk.Entry(parameter_frame)
diameter_entry.grid(row=1, column=1)
diameter_entry_button = tk.Button(parameter_frame, text = 'Send', command=send_diameter)
diameter_entry_button.grid(row=1, column = 2)


## Debug section
#Debug screen with time delay and received serial packets
debug_frame = tk.LabelFrame(root, text="Debug", height=100,width=150)
debug_frame.grid(row=5, column=4, rowspan=3, columnspan=3, padx=5, pady=5)
serial_print = tk.Label(debug_frame, text="Serial")
serial_print.grid(row=1, column=3, padx=5)


##Connection frame section
connection_frame = tk.LabelFrame(root, text="Connection (WIP)", height=50,width=150)
connection_frame.grid(row=0, column=4, rowspan=2, columnspan=2, padx=5, pady=5)

# Port selection menu

connect_button = tk.Button(connection_frame, text = "Reconnect", command=reconnect)
connect_button.grid(row=0, column=1 , padx=5)

connect_button = tk.Button(connection_frame, text = "Check Ports", command=check_ports)
connect_button.grid(row=1, column=1 , padx=5)

status_label = tk.Label(connection_frame, text = "Status: Disconnected", bg = 'red')
status_label.grid(row=1, column=0 , padx=5)

current_port = tk.StringVar()

#If COM4 is available, it picks it as default when lauching or else it picks the first one available
if "COM4" in serial_ports():
    current_port.set("COM4") 
else:
    current_port.set(serial_ports()[0]) 

connection_drop_menu = tk.OptionMenu(connection_frame, current_port, *serial_ports())
connection_drop_menu.grid(row=0, column=0,columnspan=1, padx=5)


def checkSerialPort():
    """Check serial input from the arduino and put the value back into the corresponding label. 
    String arriving from the arduino has the format "value1, value2, etc"
    """
    try: 
        # if serial communication is open and data is waiting in arduino
        if ser.isOpen() and ser.in_waiting:
            # Read the output line of the arduino and make a list of each element
            recentPacket = ser.readline()
            recentPacketString = recentPacket.decode('utf').split(",")
            
            # Update the value for each printed values if its a float (can be an altered value)
            try:
                if isinstance(float(recentPacketString[0]), float):
                    speed_capstan.config(text= "Speed : " + recentPacketString[0])
                if isinstance(float(recentPacketString[1]), float):
                    speed_preform.config(text= "Speed : " + recentPacketString[1])
                if isinstance(float(recentPacketString[2]), float):
                    speed_spool.config(text= "Speed : " + recentPacketString[2])
                if isinstance(float(recentPacketString[3]), float):

                    diameter.config(text= "Diameter : " + recentPacketString[3])
                
                #Outputs the delay and serial packet info on the GUI (for testing)
                serial_print.config(text = "Serial: " + "' '".join(recentPacketString))
            except IndexError:
                pass
                
    # Try to avoid bad bytes
    except UnicodeDecodeError:
        pass
running = True


### Main program loop

def initialise(commPort):
    global ser
    if commPort == "None":
        status_label.config(text="No Available Port", bg = 'yellow')
        reconnection_loop()
    else:
        ser = serial.Serial(commPort, baudrate = 115200, timeout = 1)
        status_label.config(text="Connected", bg = 'green')


#Initialise Serial communication
initialise(current_port.get())

#Run the main program loop
program_loop()


# Close serial communication 
ser.close()


