int buzzerPin = 8; // Pin where the buzzer is connected
int ledPin1 = 9;   // Pin where the first LED is connected
int ledPin2 = 7;  // Pin where the second LED is connected


bool condition = false; // Variable to control buzzer and LEDs toggle
bool buzzerState = false; // Current state of the buzzer
bool ledState1 = false;   // Current state of the first LED
bool ledState2 = false;   // Current state of the second LED
bool ledState3 = false;   // Current state of the third LED

unsigned long previousMillis = 0; // Store the last time the buzzer and LEDs were toggled
const long interval = 100; // Interval at which to toggle the buzzer and LEDs (milliseconds)

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud rate
  pinMode(buzzerPin, OUTPUT); // Set the buzzer pin as an output
  pinMode(ledPin1, OUTPUT);   // Set the first LED pin as an output
  pinMode(ledPin2, OUTPUT);   // Set the second LED pin as an output
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read(); // Read the incoming byte
    
    if (received == '1') {
      condition = true; // Set condition to true to start the alarm
    } else if (received == '0') {
      condition = false; // Set condition to false to stop the alarm
      digitalWrite(buzzerPin, LOW); // Ensure the buzzer is off
      digitalWrite(ledPin1, LOW);   // Ensure the first LED is off
      digitalWrite(ledPin2, HIGH);   // Ensure the second LED is on

      buzzerState = false; // Reset buzzer state
      ledState1 = false;   // Reset first LED state
    }else if (received == '3'){
     digitalWrite(buzzerPin, LOW); // Ensure the buzzer is off
      digitalWrite(ledPin1, LOW);   // Ensure the first LED is off
      digitalWrite(ledPin2, LOW);   // Ensure the second LED is off
      condition = false; // Set condition to false to stop the alarm


    }
  }
  
  if (condition) {
    unsigned long currentMillis = millis();
    
    if (currentMillis - previousMillis >= interval) {
      // Save the last time the buzzer and LEDs were toggled
      previousMillis = currentMillis;
      
      // Toggle the states of the buzzer and LEDs
      buzzerState = !buzzerState;
      ledState1 = !ledState1;

      // Apply the new states
      digitalWrite(buzzerPin, buzzerState ? HIGH : LOW);
      digitalWrite(ledPin1, ledState1 ? HIGH : LOW);
   
  }
 }
}

