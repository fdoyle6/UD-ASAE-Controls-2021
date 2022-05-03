#include <Servo.h>

Servo servoP; 

void setup() {
  Serial.begin(115200);
  
  servoP.attach(13);
  servoP.write(0);
  Serial.println("setup complete");
  delay(8000);
}

void loop() {
  servoP.write(0);
  delay(1000);
  servoP.write(90);
  delay(1000);
  Serial.println("spin");
}
