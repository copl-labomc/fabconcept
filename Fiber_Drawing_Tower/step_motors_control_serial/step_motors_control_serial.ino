// script created by
//     ALEXANDRE SAGONA alsag3@ulaval.ca
// used to control steps motor for the fiber tower via pyserial


#include <AccelStepper.h>
const int cabestan_stepPin = 4;
const int cabestan_dirPin = 5;
const int preform_stepPin;
const int preform_dirPin;

const int cabestan_max_speed_ = 1000;
const int preform_max_speed_ = 1000;

char motor_preform_input;
char cabestan_motor_input;

// Creates an instance
AccelStepper cabestan_stepper(AccelStepper::DRIVER, cabestan_stepPin, cabestan_dirPin);
AccelStepper preform_stepper(AccelStepper::DRIVER, preform_stepPin, preform_dirPin);
void setup()

{
  Serial.begin(9600);
  cabestan_stepper.setMaxSpeed(1000);
}

void loop(){

  if (Serial.available() > 0) {
    cabestan_motor_input = Serial.read();
    if (cabestan_motor_input == 's') {
      while (cabestan_motor_input != 'a') {
        int sensorValue = analogRead(A0);
        float new_speed_cabestan = map((analogRead(sensorValue)), 0, 1023, 0, cabestan_max_speed_);
        cabestan_stepper.setSpeed(new_speed_cabestan);
        cabestan_stepper.runSpeed();
        cabestan_motor_input = Serial.read();
      }
    }
  } // Serial.available
  
//      int sensorValue = analogRead(A0);
//      float new_speed_cabestan = map((analogRead(sensorValue)), 0, 1023, 0, cabestan_max_speed_);
//      cabestan_stepper.setSpeed(new_speed_cabestan);
//      cabestan_stepper.runSpeed();
//      Serial.println(new_speed_cabestan);
}
