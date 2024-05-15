#include <AccelStepper.h>

// setting all variables

// flag to see if motor is already on
bool cabestan_running = false;
bool preform_motor_running = false;

// Arduino pins for the drivers
const int cabestan_stepPin = 4;
const int cabestan_dirPin = 5;
const int preform_stepPin = 2;
const int preform_dirPin = 3;

// Speed of motors
int new_speed_cabestan;
int new_speed_preform; 

// Diameter variables
float offset = 0.07;
float diameter_tension;
float conversion_factor_diameter_tension = 0.5;
float real_diameter = 0;

const int cabestan_max_speed = 999;
const int preform_max_speed = 999;

// input of the python app
char motor_preform_dir;

String received_diameter_string = "";
float desired_diameter = 0;

// Creates an instance for both motors
AccelStepper cabestan_stepper(AccelStepper::DRIVER, cabestan_stepPin, cabestan_dirPin);
AccelStepper preform_stepper(AccelStepper::DRIVER, preform_stepPin, preform_dirPin);

// map function working with float 
float mapf(float value, float fromLow, float fromHigh, float toLow, float toHigh) {
  float result;
  result = (value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow;
  return result;
} 

// Function adjusting the cabestan motor speed with the value measured trought the potentiometer
void controlCabestan(int cabestan_speed) {
  cabestan_stepper.setSpeed(cabestan_speed);
  cabestan_stepper.runSpeed();
}

// Function adjusting the preform motor speed and its direction depending the button pressed
void controlPreformMotor(char dir, int preform_speed) {
  if (dir == 't'){
  preform_stepper.setSpeed(preform_speed);
  preform_stepper.runSpeed();
  }
   if (dir == 'b'){
  preform_stepper.setSpeed(-preform_speed);
  preform_stepper.runSpeed();
  }
}


void setup() {
  // Initilization of serial port
  Serial.begin(9600);
  // Setting max speed of the motors to avoid damages
  cabestan_stepper.setMaxSpeed(cabestan_max_speed);
  preform_stepper.setMaxSpeed(preform_max_speed);
}

// Main loop
void loop() {
  if (Serial.available() > 0) {
    
    char command = Serial.read();
    // Depending of the byte received (a char) and if the motor is not active turn it on 
    // or off and change the flags status
    
    if (command == 's' && !cabestan_running) {
      cabestan_running = true;
    }

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
      new_speed_preform = 0;
    } 
    
    else if (isPunct(command) || isDigit(command)) {
      received_diameter_string += command;
    }

    else if (command == 'e') {
      desired_diameter = received_diameter_string.toFloat();
      received_diameter_string = "";
    }
  }
  // if flag for the cabestan is true read the tension of potentiometer to adapt the speed
  if (cabestan_running) {
    int sensorValue = analogRead(A0);
    new_speed_cabestan = map(sensorValue, 0, 1023, 0, cabestan_max_speed);
    controlCabestan(new_speed_cabestan);
    
  }
  // if flag for the preform is true read the tension of potentiometer to adapt the speed
  if (preform_motor_running) {
    int sensor2Value = analogRead(A1);
    new_speed_preform = map(sensor2Value, 0, 1023, 0, preform_max_speed);
    controlPreformMotor(motor_preform_dir, new_speed_preform);
  }
  // Read the sensor value of diameter and cinvert it to mm
  float diameter_sensor = analogRead(A2);
  diameter_tension = mapf(diameter_sensor, 0, 1023, 0.0, 5.0);
  real_diameter = diameter_tension / conversion_factor_diameter_tension + offset;
  // Sending output values to the python application

  Serial.print(new_speed_cabestan);
  Serial.print(",");
  Serial.print(new_speed_preform);
  Serial.print(",");
  Serial.print(real_diameter);
  Serial.print(",");
  Serial.println(desired_diameter, 2);
  
}
