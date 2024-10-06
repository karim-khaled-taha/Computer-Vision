#include <IRremote.h>
#include "Stepper.h"

#define STEPS  32  // Number of steps per revolution of Internal shaft

int Steps2Take;  // 2048 = 1 Revolution

// Setup of proper sequencing for Motor Driver Pins
// In1, In2, In3, In4 in the sequence 1-3-2-4
Stepper small_stepper(STEPS, 8, 10, 9, 11);
int enA = 10;
int in1 = 8;
int in2 = 9;
// pinky
int enA_pinky = 4;
int in1_pinky = 2;
int in2_pinky = 3;



IRrecv IR(7);
const int ldrPin = A0;  

#define m1 9
#define horn 12
int Y_Led_1 = 3;
int Y_Led_2 = 4;
int Y_Led_3 = 5;
int Y_Led_4 = 11;
int m_state=0;
int m1_state=0;
int m2_state=0;
int m3_state=0;
int m4_state=0;
int m5_state=0;

int horn_state=0;
bool condition = false; // Variable to control LED toggle


void setup()
{
  Serial.begin(9600);
  IR.enableIRIn();
  pinMode(ldrPin, INPUT);    
  pinMode(m1,OUTPUT);
  pinMode(horn,OUTPUT);
  pinMode(Y_Led_1, OUTPUT);
  pinMode(Y_Led_2, OUTPUT);
  pinMode(Y_Led_3, OUTPUT);
  pinMode(Y_Led_4, OUTPUT);

}

void loop()
{
  
  
  if (IR.decode()) {
    Serial.println(IR.decodedIRData.decodedRawData);

    if (IR.decodedIRData.decodedRawData == 3977428800 && m_state==0 ) {
      // Turn on LEDR when the corresponding button is pressed
      digitalWrite(Y_Led_1, HIGH);
      delay(1000); // Delay for stabilization
      digitalWrite(Y_Led_1, LOW);
      m1_state = 1 ;
      //IR.decodedIRData.decodedRawData = 0 ;
    } else if (IR.decodedIRData.decodedRawData == 4261527360 && m1_state == 0 ) {   // thump finger close  
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, 255); // Adjust speed (0-255) as needed
      delay(300); // Run for 2 seconds
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      m1_state = 1 ;
      //IR.decodedIRData.decodedRawData = 0 ;
    }  else if (IR.decodedIRData.decodedRawData == 4244815680 && m2_state == 0 ) {  // index finger close
       condition = !condition; // Toggle the LED state
       //IR.decodedIRData.decodedRawData = 0 ;
    }else if (IR.decodedIRData.decodedRawData == 4228104000 && m3_state == 0 ) {   // middle finger close  
      // Turn on LEDG when the corresponding button is pressed
      digitalWrite(horn, HIGH);
      horn_state = 1 ;
      //IR.decodedIRData.decodedRawData = 0 ;
    }  else if (IR.decodedIRData.decodedRawData == 4211392320 &&  m4_state == 0) {  // ring finger close
       condition = !condition; // Toggle the LED state
       //IR.decodedIRData.decodedRawData = 0 ;
    }  else if (IR.decodedIRData.decodedRawData == 4194680640  && m5_state == 0) {  // pinky finger close
       digitalWrite(in1_pinky, HIGH);
       digitalWrite(in2_pinky, LOW);
       analogWrite(enA_pinky, 150); // Adjust speed (0-255) as needed
       delay(50); // Run for 2 seconds  
        digitalWrite(in1_pinky, LOW);
       digitalWrite(in2_pinky, LOW);
        m5_state = 1 ;       
    }else {
      // Additional conditions to turn off each LED individually
      if ( IR.decodedIRData.decodedRawData == 3977428800 && m_state ==1) {
        digitalWrite(Y_Led_2, HIGH);
        delay(1000); // Delay for stabilization
        digitalWrite(Y_Led_2, LOW);
        m1_state = 0 ;
       //IR.decodedIRData.decodedRawData = 0 ;

      } if ( IR.decodedIRData.decodedRawData ==4261527360 &&  m1_state == 1) {  // thump finger opean
         digitalWrite(in1, LOW);
         digitalWrite(in2, HIGH);
         analogWrite(enA, 255); // Adjust speed (0-255) as needed
         delay(200); // Run for 2 seconds
         digitalWrite(in1, LOW);
         digitalWrite(in2, LOW);
         m1_state = 0 ;
    
      }if (IR.decodedIRData.decodedRawData == 4244815680 && m2_state == 1  ) {   // index finger opean
       condition = false; // Turn off the LED and break the loop
   
      } if ( IR.decodedIRData.decodedRawData ==4228104000 &&  m3_state == 1) {  // middle finger opean 
        digitalWrite(horn, LOW);
        horn_state = 1 ;
      } if ( IR.decodedIRData.decodedRawData ==4211392320 &&  m4_state == 1) {   // ring finger opean
        digitalWrite(horn, LOW);
        horn_state = 1 ;
      } if ( IR.decodedIRData.decodedRawData == 4194680640 &&  m5_state == 1) {  // pinky finger opean
        digitalWrite(in1_pinky, LOW);
        digitalWrite(in2_pinky, HIGH);
        analogWrite(enA_pinky, 150); // Adjust speed (0-255) as needed
        delay(30); // Run for 2 seconds  
        digitalWrite(in1_pinky, LOW);
        digitalWrite(in2_pinky, LOW);
        m5_state = 0 ;
      }
    }
    delay(1500);
    IR.resume();
  
  }
   
  }

