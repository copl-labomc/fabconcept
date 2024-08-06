#include <AccelStepper.h>

// setting all variables

// flag to see if motor is already on
bool capstan_running = false;
bool preform_motor_running = false;
bool spool_running = false;

// automatic 
bool automatic = false;

// Make sure the spool turns the right way when it starts
int reversed = -1;

// Arduino pins for the drivers
const int capstan_stepPin = 6;
const int capstan_dirPin = 7;

const int preform_stepPin = 10;
const int preform_dirPin = 11;

const int spool_stepPin = 4;
const int spool_dirPin = 5;

const int relay_pin = 2;


// Speed of motors
int new_speed_capstan;
int new_speed_preform; 
int new_speed_spool; 

// Diameter variables
float offset = 0.07;
float diameter_tension;
float conversion_factor_diameter_tension = 0.5;
float real_diameter = 0;

const int capstan_max_speed = 999;
const int preform_max_speed = 999;
const int spool_max_speed = 999;

// character received from serial connection from laptop
char command;

// counter that counts to 1000 so that the heavy calculations are done only once per 1000 loops
int count;

// Timer that stop motors and oven after a certain time
int shutdown_timer;


// Number of iterations before stopping motors when nothing happens
// 10000 = About 1 minute
int shutdown_limit = 10000;

// input of the python app
char motor_preform_dir;

// For the instructions larger than one character, they are stored as a string until said instruction is complete
String received_string = "";

// Config info
float desired_diameter;
float drawing_constant;
float capstan_diameter;
float spool_circumeference;
int microstepping;

// Creates an AccelStepper instance for the three motors
AccelStepper capstan_stepper(AccelStepper::DRIVER, capstan_stepPin, capstan_dirPin);
AccelStepper preform_stepper(AccelStepper::DRIVER, preform_stepPin, preform_dirPin);
AccelStepper spool_stepper(AccelStepper::DRIVER, spool_stepPin, spool_dirPin);

// map function working with float 
float mapf(float value, float fromLow, float fromHigh, float toLow, float toHigh) {
  float result;
  result = (value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow;
  return result;
} 

// Function adjusting the capstan motor speed
void controlCapstan(int capstan_speed) {
  capstan_stepper.setSpeed(capstan_speed);
  capstan_stepper.runSpeed();
}

// Function adjusting the spool motor speed and direction
void controlSpool(int rev, int spool_speed) {
  spool_stepper.setSpeed(spool_speed * rev);
  spool_stepper.runSpeed();
  
}

// Function adjusting the preform motor speed and direction
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

// Calls the runSpeed() function for all running motors. This function needs to be called as much as possible to ensure smooth rotation
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
  pinMode(relay_pin, OUTPUT);
  digitalWrite(relay_pin, HIGH);
}

// Main loop
void loop() {
  // Constantly check if a command is sent from the computer
  if (Serial.available() > 0) {
    command = Serial.read();

    // If the command is a float or int, each digit is sent one at a time
    // This line checks if it is a digit or a period character and
    // adds it to a string
    if (isPunct(command) || isDigit(command)) {
      received_string += command;
    }
    // Once an end character 'e', 'f', 'g', 'h' or 'i' is received, the string is converted to a float (or int)
    // and stored into memory

    // See the python code documentation for the list of instructions
    else if (command == 'e') {
      desired_diameter = received_string.toFloat();
      received_string = "";
      // When a diameter instruction is received, starts automatic mode
      automatic = true;
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
      spool_circumeference = received_string.toFloat();
      received_string = "";
    }
    else if (command == 'i') {
      microstepping = received_string.toFloat();
      received_string = "";
    }
    else if (command == 's' && !capstan_running) {
      capstan_running = true;
    }

     else if (command == 'a') {
      capstan_running = false;
      new_speed_capstan = 0;
      automatic = false;
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
      automatic = false;
    }
    
    else if (command == 'q') {
      spool_running = false;
      new_speed_spool = 0;
      automatic = false;
    } 

    else if (command == 'w' && !spool_running) {
      spool_running = true;
    } 

    else if (command == 'r') {
      spool_running = true;
      reversed = reversed * -1;
    } 
  }
  // Only run this part once every 1000 loops
  if (count > 1000){

    // If every motor is off
    if (!(capstan_running || spool_running || preform_motor_running)) {
      shutdown_timer += 1;
    } else {
      shutdown_timer = 0;
    }

    if (shutdown_timer >= shutdown_limit) {
      digitalWrite(relay_pin, LOW);
    } else {
      digitalWrite(relay_pin, HIGH);
    }


    if (!automatic) {
      
      // In manual mode
      // if flag for the capstan is true read the voltage of potentiometer to adapt the speed
      if (capstan_running) {
        
        int sensorValue = analogRead(A0);
        new_speed_capstan = map(sensorValue, 0, 1023, 0, capstan_max_speed);
        controlCapstan(new_speed_capstan);
      } 

      if (spool_running) {
        int sensor3Value = analogRead(A0);
        new_speed_spool = map(sensor3Value, 0, 1023, 0, spool_max_speed) * capstan_diameter / spool_circumeference * 3.14159;
        controlSpool(reversed, new_speed_spool);
      }

      // if flag for the preform is true read the tension of potentiometer to adapt the speed
      if (preform_motor_running) {
        int sensor2Value = analogRead(A1);
        new_speed_preform = map(sensor2Value, 0, 1023, 0, preform_max_speed);
        //new_speed_preform = 999;
        controlPreformMotor(motor_preform_dir, new_speed_preform);
      }
    } if (automatic) {
      // In automatic mode, the speeds are calculated using the config and sent information
      // Capstan speed is fixed
      new_speed_capstan = 500; 
      //Spool speed is synced with the capstan's speed
      new_speed_spool = new_speed_capstan * capstan_diameter / spool_circumeference * 3.14159;
      // The preform speed is calculated using the equation
      // Vp = Df^2/Dp^2 * Vc
      // With some conversion factors
      new_speed_preform = 999 * 3.14159 * desired_diameter * desired_diameter * capstan_diameter * new_speed_capstan / microstepping / drawing_constant;

      // Start all motors
      preform_motor_running = true;
      spool_running = true;
      capstan_running = true;
      controlCapstan(new_speed_capstan);
      controlSpool(-1, new_speed_spool);
      controlPreformMotor('b', new_speed_preform);
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
    // Run the runSpeed command multiple times because the Serial print operation messes with the stepper motor's timing    
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
    Serial.println(real_diameter);

    count = 0;
  }
  stepTheMotors();
  count += 1;
}
