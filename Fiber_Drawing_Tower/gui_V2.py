import tkinter as tk
import serial
from tkinter import ttk


### CONNECTION SECTION 

commPort = 'COM4'
global ser
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)
def close_window():
  global running
  running = False  # turn off while loop
  ser.close()

### GUI
 
root = tk.Tk()
root.title("Fiber Tower")
root.geometry("500x300")
root.protocol("WM_DELETE_WINDOW", close_window)
# # Simply set the theme
# root.tk.call("source", r"Azure-ttk-theme-main\azure.tcl")
# root.tk.call("set_theme", "dark")

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



# Création des boutons
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

# #creation output 
speed_preform = tk.Label(preform_frame, text="Speed :")
speed_preform.grid(row=3, column=0, padx=5)

## CABESTAN STEPPER SECTION 
cabestan_frame = tk.LabelFrame(root, text="Cabestan Motor", height=100,width=150)
cabestan_frame.grid(row=4, column=0, rowspan=3, columnspan=3)

# Button functions
def start_cabestan():
    ser.write(b's')
def stop_cabestan():
    ser.write(b'a')
    
# Création du bouton Start en vert
button_start = tk.Button(cabestan_frame, text="Start", command=start_cabestan, font=("Segoe Ui", 12), bg="green", fg="white")
button_start.grid(row=0, column=0, padx=5)

# Création du bouton Stop en rouge
button_stop = tk.Button(cabestan_frame, text="Stop", command=stop_cabestan, font=("Segoe Ui", 12), bg="red", fg="white")
button_stop.grid(row=0, column=1, padx=5)

# Valeur de vitesses 


speed_cabestan = tk.Label(cabestan_frame, text="Speed:")
speed_cabestan.grid(row=1, column=0, padx=5)


## Parameter frame section 
parameter_frame = tk.LabelFrame(root, text="Parameters", height=100,width=150)
parameter_frame.grid(row=0, column=4, rowspan=3, columnspan=3, padx=5, pady=5)
diameter = tk.Label(parameter_frame, text="Diameter :")
diameter.grid(row=0, column=0, padx=5)




def checkSerialPort():
    try: 
        if ser.isOpen() and ser.in_waiting:
            recentPacket = ser.readline()
            recentPacketString = recentPacket.decode('utf').split(",")
            try : 
                speed_cabestan.config(text= "Speed : " + recentPacketString[0])
                speed_preform.config(text= "Speed : " + recentPacketString[1])
                diameter.config(text= "Diameter : " + recentPacketString[2] + "mm")
            except:
                pass
    except UnicodeDecodeError:
        pass
running = True;
while True:
    root.update()
    if not running: 
        break
    checkSerialPort()


