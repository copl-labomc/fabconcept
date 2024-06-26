import tkinter as tk
import serial
from tkinter import ttk


### CONNECTION SECTION 
# create a COM4 communication "ideally" this should be a droplist menu 

commPort = 'COM4'
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
    
# Création du bouton Start en vert
button_start = tk.Button(cabestan_frame, text="Start", command=start_cabestan, font=("Segoe Ui", 12), bg="green", fg="white")
button_start.grid(row=0, column=0, padx=5)

# Création du bouton Stop en rouge
button_stop = tk.Button(cabestan_frame, text="Stop", command=stop_cabestan, font=("Segoe Ui", 12), bg="red", fg="white")
button_stop.grid(row=0, column=1, padx=5)

# Printing output speed of cabestan

speed_cabestan = tk.Label(cabestan_frame, text="Speed:")
speed_cabestan.grid(row=1, column=0, padx=5)


## Parameter frame section 
parameter_frame = tk.LabelFrame(root, text="Parameters", height=100,width=150)
parameter_frame.grid(row=0, column=4, rowspan=3, columnspan=3, padx=5, pady=5)

# printing diameter measured by laser sensor
diameter = tk.Label(parameter_frame, text="Diameter Measurement:")
diameter.grid(row=0, column=0,columnspan=4, padx=5)
# input for the diameter desired
diameter_desired = tk.Label(parameter_frame, text='Diameter desired :')
diameter_desired.grid(row=1, column=0)
diameter_entry = tk.Entry(parameter_frame)
diameter_entry.grid(row=1, column=1)



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
            
            try : 
                if isinstance(float(recentPacketString[0]), float):
                    speed_cabestan.config(text= "Speed : " + recentPacketString[0])
                if isinstance(float(recentPacketString[1]), float):
                    speed_preform.config(text= "Speed : " + recentPacketString[1])
                if isinstance(float(recentPacketString[2]), float):
                    # remove the formating of arduino serial.write end of line
                    diameter.config(text= "Diameter : " + recentPacketString[2].replace("\r\n", "") +" mm")
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


