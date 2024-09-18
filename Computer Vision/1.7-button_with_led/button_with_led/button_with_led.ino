  #define LEDR 6
  #define LEDO 5
  #define LEDB 7
  
  int LEDR_state=0;
  int LEDO_state=0;
  int LEDB_state=0;
  int LEDG_state=0;
  int horn_state=0;





  void setup()
  {
    Serial.begin(9600);
    pinMode(LEDR,OUTPUT);
    pinMode(LEDO,OUTPUT);
    pinMode(LEDB,OUTPUT);
    digitalWrite(LEDR, HIGH);
    delay(500);
    digitalWrite(LEDR, LOW);
      
            


  }

  void loop()
  {
    if (Serial.available() > 0) {
      char received = Serial.read();

    
    
    if (received == '1' && LEDR_state==0 ) {
        // Turn on LEDR when the corresponding button is pressed
        digitalWrite(LEDR, HIGH);
        LEDR_state = 1 ;
        received = 0 ;
      } else if (received == '2' && LEDO_state == 0  ) {
        // Turn on LEDO when the corresponding button is pressed
        digitalWrite(LEDO, HIGH);
        LEDO_state = 1 ;
        received = 0 ;
      } else if (received == '3' && LEDB_state == 0) {
        // Turn on LEDB when the corresponding button is pressed
        digitalWrite(LEDB, HIGH);
        LEDB_state = 1 ;
       received = 0 ;
      } else {
        // Additional conditions to turn off each LED individually
        if (digitalRead(LEDR) == HIGH && received == '1' && LEDR_state ==1) {
          digitalWrite(LEDR, LOW);
          LEDR_state = 0 ;
         received = 0 ;

        }if (digitalRead(LEDO) == HIGH && received == '2' && LEDO_state == 1 ) {
          digitalWrite(LEDO, LOW);
          LEDO_state = 0 ;
       received= 0 ;

        }if (digitalRead(LEDB) == HIGH && received == '3' && LEDB_state == 1) {
          digitalWrite(LEDB, LOW);
          LEDB_state = 0 ;
        received = 0 ;

        }
      }
      delay(1500);

      } 
    
    }
    
    

