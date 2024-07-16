#include <AccelStepper.h>

// setting all variables

// flag to see if motor is already on
bool capstan_running = false;
bool preform_motor_running = false;
bool spool_running = false;

// Make sure the spool turns the right way when it starts
int reversed = -1;

// Arduino pins for the drivers
const int capstan_stepPin = 6;
const int capstan_dirPin = 7;

const int preform_stepPin = 10;
const int preform_dirPin = 11;

const int spool_stepPin = 4;
const int spool_dirPin = 5;

// Speed of motors
int new_speed_capstan;
int new_speed_preform; 
int new_speed_spool; 

// Diameter variables
float offset = 0.02;
float diameter_tension;
float conversion_factor_diameter_tension = 0.5;
float real_diameter = 0;

const int capstan_max_speed = 999;
const int preform_max_speed = 999;
const int spool_max_speed = 999;


char command;
int count;

// input of the python app
char motor_preform_dir;
char motor_spool_dir;

String received_string = "";
float desired_diameter;
float drawing_constant;
float capstan_diameter;
float spool_diameter;


// Creates an instance for both motors
AccelStepper capstan_stepper(AccelStepper::DRIVER, capstan_stepPin, capstan_dirPin);
AccelStepper preform_stepper(AccelStepper::DRIVER, preform_stepPin, preform_dirPin);
AccelStepper spool_stepper(AccelStepper::DRIVER, spool_stepPin, spool_dirPin);

// map function working with float 
float mapf(float value, float fromLow, float fromHigh, float toLow, float toHigh) {
  float result;
  result = (value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow;
  return result;
} 

// Function adjusting the capstan motor speed with the value measured trought the potentiometer
void controlCapstan(int capstan_speed) {
  capstan_stepper.setSpeed(capstan_speed);
  capstan_stepper.runSpeed();
}

void controlSpool(int rev, int spool_speed) {
  spool_stepper.setSpeed(spool_speed * rev);
  spool_stepper.runSpeed();
  
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

void stepTheMotors() {
  if (capstan_running) {
    capstan_stepper.runSpeed();
  }

  if (preform_motor_running) {
    preform_stepper.runSpeed();
  }

  if (spool_running) {
    spool_stepper.runSpeed();
  }
}

void setup() {
  // Initilization of serial port
  Serial.begin(115200);
  // Setting max speed of the motors to avoid damages
  capstan_stepper.setMaxSpeed(capstan_max_speed);
  preform_stepper.setMaxSpeed(preform_max_speed);
  spool_stepper.setMaxSpeed(spool_max_speed);
}

// Main loop
void loop() {
  // Constantly check if a command is sent from the computer
  if (Serial.available() > 0) {
    command = Serial.read();

    // If the command is a float, each digit is sent one at a time
    // This line checks if it is a digit or a period character and
    // adds it to a string
    if (isPunct(command) || isDigit(command)) {
      received_string += command;
    }
    // Once the end character 'e' is received, the string is converted to a float
    // and stored into memory
    else if (command == 'e') {
      desired_diameter = received_string.toFloat();
      received_string = "";
    }
    else if (command == 'f') {
      drawing_constant = received_string.toFloat();
      received_string = "";
    }
    else if (command == 'g') {
      capstan_diameter = received_string.toFloat();
      received_string = "";
    }
    else if (command == 'h') {
      spool_diameter = received_string.toFloat();
      received_string = "";
    }
    else if (command == 's' && !capstan_running) {
      capstan_running = true;
    }

     else if (command == 'a') {
      capstan_running = false;
      new_speed_capstan = 0;
    }

     else if (command == 't') {
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
    
    else if (command == 'q') {
      spool_running = false;
      new_speed_spool = 0;
    } 

    else if (command == 'w' && !spool_running) {
      spool_running = true;
    } 

    else if (command == 'r') {
      spool_running = true;
      reversed = reversed * -1;
    } 
  }
    // Depending of the byte received (a char) and if the motor is not active turn it on 
    // or off and change the flags status
  if (count > 1000){
    // if flag for the capstan is true read the tension of potentiometer to adapt the speed
    if (capstan_running) {
      int sensorValue = analogRead(A0);
      new_speed_capstan = map(sensorValue, 0, 1023, 0, capstan_max_speed);
      controlCapstan(new_speed_capstan);
    }

    if (spool_running) {
      int sensorValue = analogRead(A0);
      new_speed_spool = map(sensorValue, 0, 1023, 0, spool_max_speed);
      controlSpool(reversed, new_speed_spool);
    }

    // if flag for the preform is true read the tension of potentiometer to adapt the speed
    if (preform_motor_running) {
      int sensor2Value = analogRead(A1);
      new_speed_preform = map(sensor2Value, 0, 1023, 0, preform_max_speed);
      controlPreformMotor(motor_preform_dir, new_speed_preform);
    }

    //Read the analog input from the diameter sensor 10 times and add them
    float diameter_data = 0;
    for (int i = 0; i < 10; i++) {
      diameter_data += analogRead(A2);
    }

    // Divide by the number of mesurements to get average diameter
    float diameter_average = diameter_data / 10;
    
    // Convert the analog reading to mm
    diameter_tension = mapf(diameter_average, 0, 1023, 0.0, 5.0);

    real_diameter = diameter_tension / conversion_factor_diameter_tension + offset;
    // Sending output values to the python application
    // Run the runSpeed command multiple times
    stepTheMotors();
    Serial.print(new_speed_capstan);
    stepTheMotors();
    Serial.print(",");
    Serial.print(new_speed_preform);
    stepTheMotors();
    Serial.print(",");
    Serial.print(new_speed_spool);
    stepTheMotors();
    Serial.print(",");
    Serial.print(real_diameter);
    Serial.print(",");
    stepTheMotors();
    Serial.println(desired_diameter, 2); 
    stepTheMotors();

    count = 0;
  }
  stepTheMotors();
  count += 1;
}
