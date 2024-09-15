const int m1 = 6;
const int m2 = 7;
const int led1 = 10;
const int led2 = 11;
const int led3 = 12;
const int led4 = 9;
const int horn = 8;

bool condition = false ;


void setup() {
  Serial.begin(9600);
  
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(horn, OUTPUT);

  
  // Initialize LEDs to off
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);

}

void loop() {
  if (Serial.availa ble() > 0) {
    char receivedByte = Serial.read();
    
  Serial.println(receivedByte);

    switch (receivedByte) {
      
      case '2':
        digitalWrite(m1, HIGH);
        break;
      case '3':
        digitalWrite(m1, LOW);
        break;
      case '4':
        digitalWrite(m2, HIGH);
        break;
      case '5':
        digitalWrite(m2, LOW);
        break;
     
      case '8':
        digitalWrite(led1, HIGH);
        digitalWrite(led2, HIGH);
        digitalWrite(led3, HIGH);
        digitalWrite(led4, HIGH);
        break;
      case '9':
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);
        digitalWrite(led3, LOW);
        digitalWrite(led4, LOW);    
            break;
    }
  }

  
}
