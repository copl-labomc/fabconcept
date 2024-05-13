import tkinter as tk
import serial
from tkinter import ttk
import time
import serial

timer = time.time()
## CONNECTION SECTION 
# create a COM4 communication "ideally" this should be a droplist menu 

def serial_ports():
    """ Finds all the port in use and returns it as a list
    """
    
    #Try every possible port 
    ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            
            result.append(port)
            s.close()
        except (OSError, serial.SerialException):
            pass
    return result

Available_ports = serial_ports()

commPort = Available_ports[0]

global ser
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)

def close_window():
  """Close serial communication when the windows is closed"""
  global running
  running = False  # turn off while loop
  ser.close()

### GUI

# Create a tk application 

root = tk.Tk()
root.title("Fiber Tower")
root.geometry("500x300")
root.protocol("WM_DELETE_WINDOW", close_window)


## PREFORM STEPPER SECTION 

# Frame
preform_frame = tk.LabelFrame(root, text="Preform Motor", height=100,width=150)
preform_frame.grid(row=0, column=0, rowspan=3, columnspan=3, padx=5, pady=5)


# Button functions
def preform_up():
    ser.write(b't')

def preform_down():
    ser.write(b'b')

def stop_preform():
    ser.write(b'k')


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
speed_preform.grid(row=3, column=0, padx=5)


## CABESTAN STEPPER SECTION 
cabestan_frame = tk.LabelFrame(root, text="Cabestan Motor", height=100,width=150)
cabestan_frame.grid(row=4, column=0, rowspan=3, columnspan=3)

# Button functions
def start_cabestan():
    """send "s" in byte to  start cabestan motor
    """
    ser.write(b's')
def stop_cabestan():
    """send "a" in byte to stop cabestan motor
    """
    ser.write(b'a')

def send_diameter():
    """ send the desired diameter"""
    entry = diameter_entry.get()
    if entry != '':
        ser.write(entry.encode())

        ser.write(b'e')


# Création du bouton Start en vert
button_start = tk.Button(cabestan_frame, text="Start", command=start_cabestan, font=("Segoe Ui", 12), bg="green", fg="white")
button_start.grid(row=0, column=0, padx=5)

# Création du bouton Stop en rouge
button_stop = tk.Button(cabestan_frame, text="Stop", command=stop_cabestan, font=("Segoe Ui", 12), bg="red", fg="white")
button_stop.grid(row=0, column=1, padx=5)

# Printing output speed of cabestan

speed_cabestan = tk.Label(cabestan_frame, text="Speed:")
speed_cabestan.grid(row=1, column=0, padx=5)

##Connection frame section
connection_frame = tk.LabelFrame(root, text="Connection (WIP)", height=50,width=150)
connection_frame.grid(row=0, column=4, rowspan=2, columnspan=2, padx=5, pady=5)


clicked = tk.StringVar() 
  
# initial menu text 
clicked.set( "Default: COM4" ) 
connection_drop_menu = tk.OptionMenu(connection_frame, clicked, *Available_ports)
connection_drop_menu.grid(row=0, column=0,columnspan=1, padx=5)

connect_button = tk.Button(connection_frame, text = "Connect")
connect_button.grid(row=0, column=1 , padx=5)

status_label = tk.Label(connection_frame, text = "Status: Disconnected")
status_label.grid(row=1, column=0 , padx=5)

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


#Debug screen with time delay and received serial packets
debug_frame = tk.LabelFrame(root, text="Debug", height=100,width=150)
debug_frame.grid(row=5, column=4, rowspan=3, columnspan=3, padx=5, pady=5)
serial_print = tk.Label(debug_frame, text="Serial")
serial_print.grid(row=1, column=3, padx=5)
time_print = tk.Label(debug_frame, text="Time")
time_print.grid(row=1, column=3, padx=5)



def checkSerialPort():
    """Check serial input from the arduino and put the value back into the corresponding label. 
    String arriving from the arduino has the format "value1, value2, etc"
    """
    global timer
    try: 
        # if serial communication is open and data is waiting in arduino
        if ser.isOpen() and ser.in_waiting:
            # Read the output line of the arduino and make a list of each element
            recentPacket = ser.readline()
            recentPacketString = recentPacket.decode('utf').split(",")
            
            # Update the value for each printed values if its a float (can be an altered value)
            
            try : 
                
                if isinstance(float(recentPacketString[0]), float):
                    speed_cabestan.config(text= "Speed : " + recentPacketString[0])
                if isinstance(float(recentPacketString[1]), float):
                    speed_preform.config(text= "Speed : " + recentPacketString[1])
                if isinstance(float(recentPacketString[2]), float):
                    # remove the formating of arduino serial.write end of line
                    diameter.config(text= "Diameter : " + recentPacketString[2].replace("\r\n", "") +" mm")
                
                #Outputs the delay and serial packet info on the GUI (for testing)
                serial_print.config(text = "Serial: " + "' '".join(recentPacketString))
                time_print.config(text = f"Delay: {(time.time()-timer)*1000:.2f} ms")
                timer = time.time()
                
                
            except:
                pass
    # Try to avoid bad bytes
    except UnicodeDecodeError:
        pass
running = True


while True:
    root.update()
    if not running: 
        break
    checkSerialPort()

# Closer serial communication 
ser.close()


