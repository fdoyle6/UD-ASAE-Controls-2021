/*
 * ASAE On-Board Data Acquisition System Code 2021 - 2022
 * Team: Frank Doyle - Captain, Chris Czerwinski, Jack Swift, Mike Rosen
 * Github for 2021-2022 : https://github.com/fdoyle6/UD-ASAE-Controls-2021
 * Github for 2020-2021 :https://github.com/FirkinTage/UDASAE_Controls
 * The 2020-2021 code was largely used for reference for the first few revisions of this code
 */

//Importing Libraries---------------------------------------------------------------------------------------------------------------------------------------------------

#include <SPI.h> //needed for LoRa
//#include <RH_RF95.h> //LoRa Radio library (Drivers and Managers)
#include <Servo.h> //Servo Library
#include <Wire.h>     //I2C library
#include <Adafruit_LSM9DS1.h> //IMU library
#include <Adafruit_Sensor.h>  
#include <Adafruit_GPS.h> //GPS Library
#include "Adafruit_BMP3XX.h" //Altimeter library

//Declaration of Variables-----------------------------------------------------------------------------------------------------------------------------------------------
/*
//LoRa - Model: Adafruit Feather M0 LoRa (HOPERF RFM95CW)
#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3 //32u4 = 7 M0 = 3
#define RF95_FREQ 915.0     //915MHz
RH_RF95 rf95(RFM95_CS, RFM95_INT);
int16_t packetNum = 0;  //packet counter
uint8_t recvDataPacket[RH_RF95_MAX_MESSAGE_LEN];  //packet that will be received from ground station
uint8_t recvLen = sizeof(recvDataPacket);
String outputData;
*/
String outputData;
//Altimeter - Model: Adafruit BMP 390
Adafruit_BMP3XX bmp; // I2C
bool startUp = true;
#define SEALEVELPRESSURE_HPA (1013.25)
float height = 0.0, initHeight = 0.0, PADAheight = 0.0, pressure;

//IMU - Model: Adafruit LSM9DS1
Adafruit_LSM9DS1 lsm = Adafruit_LSM9DS1();
sensors_event_t accl, magneto, gyo, lsmTemp;

//GPS - Model: Adafruit Ultimate GPS
#define GPSSerial Serial1
Adafruit_GPS GPS(&GPSSerial);
// Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
// Set to 'true' if you want to debug and listen to the raw GPS sentences
#define GPSECHO  false

float GPSlat,GPSlong, GPSangle, GPSspeed;
char latDir, longDir;
uint32_t timer = millis();

//PADA Servo
#define servoPPin 10
Servo servoP;
uint8_t PADADropped;
int servoPDrop = 0;

//LEDs
#define redLED A1
#define greLED A2
#define bluLED A3

//Data Collection F'n----------------------------------------------------------------------------------------------------------------------------------------------
int collectct = 0;
bool data_collect(){
  //visualize data collection
  outputData = ""; //reset string 
  digitalWrite(bluLED,HIGH);

  //collect from Altimeter
  if(bmp.performReading()){
    pressure = bmp.pressure/100.0;
    if(collectct<5){
      initHeight = bmp.readAltitude(SEALEVELPRESSURE_HPA)*3.28084;
    }
    height = (bmp.readAltitude(SEALEVELPRESSURE_HPA)*3.28084)-initHeight; //3.28084 for meter to feet conversion
  }
  
  //collect from IMU
  lsm.read();
  lsm.getEvent(&accl, &magneto, &gyo, &lsmTemp);

  //collect from GPS
  char GPSRaw = GPS.read();
  if(GPS.newNMEAreceived()){
    if(!GPS.parse(GPS.lastNMEA())){
      Serial.println("GPS failure");
      return false;
    }
  }
  if(millis()-timer>2000){
    timer = millis();
    if(GPS.fix){
      GPSlat = GPS.latitudeDegrees;
      GPSlong = GPS.longitudeDegrees;
      latDir = GPS.lat;
      longDir = GPS.lon;
      GPSspeed = GPS.speed * 1.15078; //To convert knots to mph
      GPSangle = GPS.angle;
    }
  }
  
  //Printing for Debugging Prior to LoRa
  outputData+="Height: " + String(height,2);
  outputData+=" MagX:" + String(magneto.magnetic.x,2);
  outputData+=" MagY:" + String(magneto.magnetic.y,2);
  outputData+=" MagZ:" + String(magneto.magnetic.z,2);
  outputData+=" AccX:" + String(accl.acceleration.x,2);
  outputData+=" AccY:" + String(accl.acceleration.y,2);
  outputData+=" AccZ:" + String(accl.acceleration.z,2);
  outputData+=" lat:" + String(GPSlat,7);
  outputData+=" lon:" + String(GPSlong,7);
  outputData+=" vel:" + String(GPSspeed,2);
  
  
  Serial.println(outputData);
  
  //LoRa transmission
  /*
   * 
   */
  digitalWrite(bluLED,LOW);
  return true;
}

//Setup-------------------------------------------------------------------------------------------------------------------------------------------------------------

void setup() {
  Serial.begin(115200);
  while(!Serial){delay(1);}//comment out when not connected to serial
  Serial.println("Beginning setup...");
  Wire.begin(); //Start I2C communication
  

  //Servo
  
  //LED
  Serial.println("Initializing LEDs...");
  digitalWrite(bluLED,HIGH);
  digitalWrite(greLED,HIGH);
  digitalWrite(redLED,HIGH);
  delay(1000);
  digitalWrite(bluLED,LOW);
  digitalWrite(greLED,LOW);
  digitalWrite(redLED,LOW);
  
  //LoRa
  
  //IMU
  Serial.println("Initializing IMU...");
  if(!lsm.begin()){
    digitalWrite(greLED,HIGH);
    Serial.println("IMU init failed...");
    while(1);
  }
  lsm.setupAccel(lsm.LSM9DS1_ACCELRANGE_2G); //2G range for best resolution (we're only going to get around 1g of max accel)
  lsm.setupMag(lsm.LSM9DS1_MAGGAIN_4GAUSS); //4Gauss range for best resolution (we only need 0-1 Gauss, we'd use a 2 gauss range if we could)
  lsm.setupGyro(lsm.LSM9DS1_GYROSCALE_245DPS); //245 DPS range for best resolution (we wanted 200 DPS)
  Serial.println("IMU setup");
  
  //GPS
  Serial.println("Initializing GPS...");
  GPS.begin(9600);
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_2HZ); //2 Hz update rate (Choices: 1,2,5,10)
  GPS.sendCommand(PGCMD_ANTENNA);
  delay(1000);
  GPSSerial.println(PMTK_Q_RELEASE);
  Serial.println("GPS setup");
  
  //Altimeter
  Serial.println("Initializing Altimeter...");
  if(!bmp.begin_I2C()){
    digitalWrite(redLED,HIGH);
    Serial.println("Altimeter init failed...");
    while(1);
  }
  bmp.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  bmp.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  bmp.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  if(bmp.performReading()){
    delay(500);
    initHeight = bmp.readAltitude(SEALEVELPRESSURE_HPA) * 3.28084; //set init height (data collection function subtracts this for a delta value from baseline)
    delay(500);
  }
  Serial.println("Altimeter setup");
}

//Main Loop---------------------------------------------------------------------------------------------------------------------------------------------------------
bool collected;

void loop() {
  // put your main code here, to run repeatedly:
  collected = data_collect();
  if (collected){
    delay(200);
    collectct+=1;
  }// for testing
  //Serial.println(String(collectct));
  
}
