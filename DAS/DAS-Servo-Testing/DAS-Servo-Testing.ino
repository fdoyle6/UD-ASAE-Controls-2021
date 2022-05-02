#include <Servo.h>

Servo servoP; 

void setup() {
  Serial.begin(9600);
  
  servoP.attach(13);
  servoP.writeMicroseconds(2000);
  Serial.println("setup complete");
  delay(8000);
}

void loop() {
  servoP.writeMicroseconds(1000);
}
