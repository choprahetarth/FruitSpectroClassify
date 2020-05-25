#define ledIndicator 13
#define FruitIndicator1 12
#include <Stepper.h> // include the stepper motor library
const int stepsPerRevolution = 50; // define the least count

#include "CytronMotorDriver.h"


// Configure the motor driver.
CytronMD motor(PWM_DIR, 3, 4);  // PWM = Pin 3, DIR = Pin 4.

Stepper myStepper(stepsPerRevolution,8,9,10,11); //create an instance of the stepper motor class
int flag = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // specify the baudrate
  pinMode(ledIndicator,OUTPUT);
  pinMode(FruitIndicator1,INPUT);
  //initialize the stepperMotor at 60 RPM
  myStepper.setSpeed(60);
}
String inputVariable;

void loop() {
  // put your main code here, to run repeatedly:
  //while(!Serial.available()){
    //wait till you recieve the bytes
  //  }
   inputVariable = Serial.readString();
   if(inputVariable == "stepper" || flag==1){ ///////// DEBUG MODE OF MODE A
   while(digitalRead(FruitIndicator1)==LOW){
      myStepper.step(stepsPerRevolution);
       motor.setSpeed(20);
    } 
     motor.setSpeed(0);
    flag=1;
   Serial.println("p");
    }
   else if(inputVariable == "s"){ ////// STOP ALL FUNCTIONS 
   myStepper.step(0);
   Serial.println("p");
    }
}
