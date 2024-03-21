#include <AccelStepper.h>


bool cabestan_running = false;
bool preform_motor_running = false;
const int cabestan_stepPin = 4;
const int cabestan_dirPin = 5;
const int preform_stepPin;
const int preform_dirPin;
int new_speed_cabestan;
int new_speed_preform; 
const int cabestan_max_speed = 1000;
const int preform_max_speed_ = 1000;

char motor_preform_dir;
// Creates an instance
AccelStepper cabestan_stepper(AccelStepper::DRIVER, cabestan_stepPin, cabestan_dirPin);
AccelStepper preform_stepper(AccelStepper::DRIVER, preform_stepPin, preform_dirPin);

void controlCabestan(int cabestan_max_speed) {
  int sensorValue = analogRead(A0);
  new_speed_cabestan = map(sensorValue, 0, 1023, 0, cabestan_max_speed);
  cabestan_stepper.setSpeed(new_speed_cabestan);
  cabestan_stepper.runSpeed();
}

void controlPreformrMotor(char dir) {
  if (dir == 't'){
  cabestan_stepper.setSpeed(-preform_max_speed_);
  cabestan_stepper.runSpeed();
  }
   if (dir == 'b'){
  cabestan_stepper.setSpeed(preform_max_speed_);
  cabestan_stepper.runSpeed();
  }
}



void setup() {
  // Initialisation du port série
  Serial.begin(9600);
  cabestan_stepper.setMaxSpeed(cabestan_max_speed);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 's' && !cabestan_running) {
      cabestan_running = true;
    } else if (command == 'a') {
      cabestan_running = false;
      new_speed_cabestan = 0;
    } else if (command == 't'  && !preform_motor_running) {
      preform_motor_running = true;
      motor_preform_dir = command;
    } else if (command == 'b') {
      preform_motor_running = true;
      motor_preform_dir = command;
    }
    else if (command == 'k') {
      preform_motor_running = false;
    }
  }

  if (cabestan_running) {
    controlCabestan(cabestan_max_speed);
  }

  if (preform_motor_running) {
    controlPreformrMotor(motor_preform_dir);
  }
  new_speed_preform = preform_max_speed_;
  Serial.print(new_speed_cabestan);
  Serial.print(",");
  Serial.println(new_speed_preform);
}
