/*
 * ASAE Ground Station Code 2021 - 2022
 * Team: Frank Doyle - Captain, Chris Czerwinski, Jack Swift, Mike Rosen
 * Github for 2021-2022 : https://github.com/fdoyle6/UD-ASAE-Controls-2021
 * Github for 2020-2021 :https://github.com/FirkinTage/UDASAE_Controls
 * The 2020-2021 code was largely used for reference for the first few revisions of this code
 */

//Importing Libraries-----------------------------------------------------------------------

#include <SPI.h>
#include <RH_RF95.h>

//Declaration of Variables------------------------------------------------------------------

//LoRa - Model: Adafruit Feather M0 LoRa
#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3
#define RF95_FREQ 915.0
RH_RF95 rf95(RFM95_CS, RFM95_INT);

//LED & Button
#define buttonPin 12
#define PADALED A1 //10 - BLUE
#define LED A0 //9 - RED

//
bool dropped = false;
bool dropConfirm = false;
int buttonState;

void send_drop()
{
  char sig[5] = "drop";
  sig[4] = 0;
  dropped = rf95.send((uint8_t *)sig, 5);
  rf95.waitPacketSent();
  delay(100);
  digitalWrite(PADALED, HIGH);
  //Serial.println("drop");
  
}
void setup()
{
  //Serial.println("initializing code");
  pinMode(LED, OUTPUT);
  pinMode(PADALED, OUTPUT);
  pinMode(buttonPin, INPUT);
  digitalWrite(PADALED,LOW);
  digitalWrite(LED,LOW);
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  Serial.begin(115200);
  //while (!Serial) {
  //  delay(1);
  //}
  delay(100);
  
  Serial.println("LoRa Initializing...");
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }
  //Serial.println("LoRa setup");
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  rf95.setTxPower(23, false);
  //Serial.println("Initialization complete");
}
uint32_t timer;
void loop()
{
  if (rf95.available())
  { 
    // Should be a message for us now
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf95.recv(buf, &len)&&len>0)
    {
      buf[len] = 0;
      digitalWrite(LED, HIGH);
      char* pckt = (char*) &buf;
      //Serial.print("Got: ");
      Serial.println(pckt);
      dropConfirm = pckt[strlen(pckt)-1]=='1'?true:false;
      //Serial.print("RSSI: ");
      //Serial.println(rf95.lastRssi(), DEC);
      digitalWrite(LED, LOW);
    }
    else
    {
      //Serial.println("Receive failed");
    }
  }
  if(!dropped){
    buttonState = digitalRead(buttonPin);
    if(buttonState==HIGH){
      send_drop();
      timer = millis();
    }
  }
  if(dropped && !dropConfirm){ //In Case Drop is not heard on first go through
    if(millis()-timer>1000){
      send_drop();
      timer = millis();
    }
  }
}
