// script created by 
//     ALEXANDRE SAGONA alsag3@ulaval.ca
// used to control steps motor for the fiber tower via pyserial


#include <AccelStepper.h>
const int cabestan_stepPin = 4;
const int cabestan_dirPin = 5;
const int max_speed_ = 1000;
char motor_preform_input;
char cabestan_motor_input;

// Creates an instance
AccelStepper  cabestan_stepper(AccelStepper::DRIVER, cabestan_stepPin, cabestan_dirPin);
void setup()

{ 
  Serial.begin(9600);  
  cabestan_stepper.setMaxSpeed(0);
}

void loop()
{  int sensorValue = analogRead(A0);
   float new_speed= map((analogRead(sensorValue)),0,1023,0,max_speed_);
   cabestan_stepper.setSpeed(new_speed);
   cabestan_stepper.runSpeed(); 
   Serial.println(new_speed);
}
