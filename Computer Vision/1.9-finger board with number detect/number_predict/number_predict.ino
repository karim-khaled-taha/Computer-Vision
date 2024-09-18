// Define the pins for the 10 LEDs
const int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

void setup() {
  // Initialize the LED pins as OUTPUT
  for (int i = 0; i < 10; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], HIGH);  // Turn on the LED
  }
  
  delay(1000);  // Keep the LEDs on for 1 second

  // Turn off all LEDs
  for (int i = 0; i < 10; i++) {
    digitalWrite(ledPins[i], LOW);  // Turn off the LED
  }
  
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();  // Read the incoming byte
    int receivedNumber = receivedChar - '0';  // Convert char to int

    if (receivedNumber >= 0 && receivedNumber <= 9) {
      updateLEDs(receivedNumber);
    }
  }
}

void updateLEDs(int number) {
  // Turn off all LEDs
  for (int i = 0; i < 10; i++) {
    digitalWrite(ledPins[i], LOW);
  }

  // If the number is 0, keep all LEDs off
  if (number == 0) {
    return;
  }

  // Turn on LEDs from 0 to the received number - 1
  for (int i = 0; i < number; i++) {
    digitalWrite(ledPins[i], HIGH);
  }
}
