const int thumbLedPin = 3;
const int indexLedPin = 4;
const int middleLedPin = 5;
const int ringLedPin = 6;
const int pinkyLedPin = 7;

void setup() {
  Serial.begin(9600);
  
  pinMode(thumbLedPin, OUTPUT);
  pinMode(indexLedPin, OUTPUT);
  pinMode(middleLedPin, OUTPUT);
  pinMode(ringLedPin, OUTPUT);
  pinMode(pinkyLedPin, OUTPUT);
  
  // Initialize LEDs to off
  digitalWrite(thumbLedPin, LOW);
  digitalWrite(indexLedPin, LOW);
  digitalWrite(middleLedPin, LOW);
  digitalWrite(ringLedPin, LOW);
  digitalWrite(pinkyLedPin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedByte = Serial.read();

    switch (receivedByte) {
      case '0':
        digitalWrite(thumbLedPin, HIGH);
        break;
      case '1':
        digitalWrite(thumbLedPin, LOW);
        break;
      case '2':
        digitalWrite(indexLedPin, HIGH);
        break;
      case '3':
        digitalWrite(indexLedPin, LOW);
        break;
      case '4':
        digitalWrite(middleLedPin, HIGH);
        break;
      case '5':
        digitalWrite(middleLedPin, LOW);
        break;
      case '6':
        digitalWrite(ringLedPin, HIGH);
        break;
      case '7':
        digitalWrite(ringLedPin, LOW);
        break;
      case '8':
        digitalWrite(pinkyLedPin, HIGH);
        break;
      case '9':
        digitalWrite(pinkyLedPin, LOW);
        break;
    }
  }
}
