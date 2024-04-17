#include <uStepperSLite.h>

uStepperSLite stepper;
const int PWM_PIN = A0;
const int NUM_SAMPLES = 1000; // Nombre d'échantillons à utiliser pour le moyennage
float val = 0;

void setup() {
  // put your setup code here, to run once:
  stepper.setup();
  stepper.setMaxAcceleration(1000);
  stepper.setMaxVelocity(1500);
  stepper.runContinous(CCW);
  Serial.begin(9600);
  // Configure le pin PWM comme entrée
  pinMode(PWM_PIN, INPUT);
  // Initialise la communication série
  Serial.begin(9600);
}

void loop() {
  val = analogRead(PWM_PIN);
  float sum = 0;
  // Lire NUM_SAMPLES échantillons du signal PWM sur le pin 9 et les stocker dans le tampon
  for (int i = 0; i < NUM_SAMPLES; i++) {
    sum += analogRead(PWM_PIN);
    delay(1); // Attendre un court instant pour éviter d'échantillonner trop rapidement
  }
  // Calculer la moyenne des échantillons
  float averageValue = 0;
  averageValue = sum/NUM_SAMPLES;
  
  // Afficher la valeur moyenne sur le moniteur série
  // Serial.println(averageValue);
  // stepper.setMaxVelocity(averageValue);
  Serial.println("Average : ");
  Serial.println(averageValue);
  // Serial.println(100000*(averageValue/1024));
  stepper.setMaxVelocity(50000*(averageValue/1024));
  // Attendre un moment avant de répéter
  delay(100);
}
