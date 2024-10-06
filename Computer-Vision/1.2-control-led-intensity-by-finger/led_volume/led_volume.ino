const int ledPin = 5;  // Connect the LED to a PWM pin

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command character
    if (command == 'L') {
      int ledLevel = Serial.parseInt(); // Read the LED level as an integer
      // Print LED level for debugging
      Serial.print("LED Level Received: ");
      Serial.println(ledLevel);
      // Map the LED level to PWM brightness (0-255)
      int brightness = map(ledLevel, 0, 100, 0, 255);
      analogWrite(ledPin, brightness); // Set the LED brightness
    }
  }
}
