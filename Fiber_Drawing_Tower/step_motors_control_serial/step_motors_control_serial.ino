// script created by
//     ALEXANDRE SAGONA alsag3@ulaval.ca
// used to control steps motor for the fiber tower via pyserial

#include <AccelStepper.h>

// Creates flags to inform about the status of motors
bool cabestan_running = false;
bool preform_motor_running = false;

// Pins for the cabestan's driver
const int cabestan_stepPin = 4;
const int cabestan_dirPin = 5;

// Pins for the preform's motor
const int preform_stepPin;
const int preform_dirPin;

// Max and actual speed of the motors
int new_speed_cabestan=0;
int new_speed_preform=0; 
const int cabestan_max_speed = 1000;
const int preform_max_speed_ = 1000;

// Creates an instance for the motors
AccelStepper cabestan_stepper(AccelStepper::DRIVER, cabestan_stepPin, cabestan_dirPin);
AccelStepper preform_stepper(AccelStepper::DRIVER, preform_stepPin, preform_dirPin);

// Function to control the cabestan by using the potentiometer's value
void controlCabestan(int new_speed_cabestan) {
  cabestan_stepper.setSpeed(new_speed_cabestan);
  cabestan_stepper.runSpeed();
}


// Function to control the motor of the preform by making it go (CW) clockwise or (ACW) anticlockwise depending 
// of the command send by the python application
void controlPreformrMotor(char dir) {
  //top (CW) when the byte 't' is received
  if (dir == 't'){
  cabestan_stepper.setSpeed(-preform_max_speed_);
  cabestan_stepper.runSpeed();
  }
  //bottom (ACW) when the byte 'b' is received
   if (dir == 'b'){
  cabestan_stepper.setSpeed(preform_max_speed_);
  cabestan_stepper.runSpeed();
  }
}



void setup() {
  // Initialisation du port série
  Serial.begin(9600);
  // Set the max speed of the motors
  cabestan_stepper.setMaxSpeed(cabestan_max_speed);
}

void loop() {
  // Open the serial communication arduino if the application is up
  if (Serial.available() > 0) {
      // Read input send by the python application 
      char command = Serial.read();
      // if "s" is received active the cabestan flag
      if (command == 's' && !cabestan_running) {
        cabestan_running = true;
      } 
     // if "a" is received deactivate the cabestan flag 
      else if (command == 'a') {
        cabestan_running = false;
        new_speed_cabestan = 0; 
      } 
      
      else if (command == 't'  && !preform_motor_running) {
        preform_motor_running = true;
        motor_preform_dir = command;
      } 
      else if (command == 'b') {
        preform_motor_running = true;
        motor_preform_dir = command;
      }
      
      else if (command == 'k') {
        preform_motor_running = false;
      }
  }

  if (cabestan_running) {
    int sensorValue = analogRead(A0);
    new_speed_cabestan = map(sensorValue, 0, 1023, 0, cabestan_max_speed);
    controlCabestan(new_speed_cabestan);
    
  }

  if (preform_motor_running) {
    controlPreformrMotor(motor_preform_dir);
  }
  new_speed_preform = preform_max_speed_;
  Serial.print(new_speed_cabestan);
  Serial.print(",");
  Serial.println(new_speed_preform);
}
