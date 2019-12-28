#define ledIndicator 13
#include "SparkFun_AS7265X.h" 
AS7265X sensor;
#include <Wire.h>

String inputVariable;
int readFlag = 5;

void setup() {
  Serial.begin(9600);
  pinMode(ledIndicator, OUTPUT);
  if(sensor.begin() == false)
  {
    Serial.println("Sensor does not appear to be connected. Please check wiring. Freezing...");
    while(1);
  }
  
  Serial.println("A,B,C,D,E,F,G,H,I,J,K,L,R,S,T,U,V,W");
}

void initiator(int a){
  if (a == 1 && initiationFlag == 1){
  inputVariable = Serial.readString();
  if (inputVariable == 'm') {
    digitalWrite(ledIndicator, HIGH);
  }
  delay(100);
  Serial.println("XCommunication Initiated"); // write a string
  initiationFlag = 0;
  }
  else if (a == 0 && finalizationFlag == 0){
   Serial.println("Communication Stopped");
   digitalWrite(ledIndicator, LOW);
   sensor.disableIndicator();
    }
}

void measure(){
  if (readFlag == 1){
    sensor.takeMeasurementsWithBulb(); //This is a hard wait while all 18 channels are measured
    Serial.print(sensor.getCalibratedA());
    Serial.print(",");
    Serial.print(sensor.getCalibratedB());
    Serial.print(",");
    Serial.print(sensor.getCalibratedC());
    Serial.print(",");
    Serial.print(sensor.getCalibratedD());
    Serial.print(",");
    Serial.print(sensor.getCalibratedE());
    Serial.print(",");
    Serial.print(sensor.getCalibratedF());
    Serial.print(",");
    Serial.print(sensor.getCalibratedG());
    Serial.print(",");
    Serial.print(sensor.getCalibratedH());
    Serial.print(",");
    Serial.print(sensor.getCalibratedI());
    Serial.print(",");
    Serial.print(sensor.getCalibratedJ());
    Serial.print(",");
    Serial.print(sensor.getCalibratedK());
    Serial.print(",");
    Serial.print(sensor.getCalibratedL());
    Serial.print(",");
    Serial.print(sensor.getCalibratedR());
    Serial.print(",");
    Serial.print(sensor.getCalibratedS());
    Serial.print(",");
    Serial.print(sensor.getCalibratedT());
    Serial.print(",");
    Serial.print(sensor.getCalibratedU());
    Serial.print(",");
    Serial.print(sensor.getCalibratedV());
    Serial.print(",");
    Serial.print(sensor.getCalibratedW());
    Serial.print(",");
    Serial.println();
    readFlag = 0;
    }
  }


 
void loop() {
  initiator(1);
  measure();
}

