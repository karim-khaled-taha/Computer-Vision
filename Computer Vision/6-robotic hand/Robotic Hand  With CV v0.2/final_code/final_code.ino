#include <Servo.h>

#define NUM_SERVOS 5

// Define servo pins
int servoPins[NUM_SERVOS] = {3, 5, 6, 9, 10}; // Pins connected to the servos

// Create an array of Servo objects
Servo servos[NUM_SERVOS];

// Initialize servo positions
int servoPositions[NUM_SERVOS] = {0, 0, 0, 0, 0}; // Positions for the 5 servos

void setup() {
  Serial.begin(9600); // Initialize serial communication
  
  // Attach each servo to its respective pin
  for (int i = 0; i < NUM_SERVOS; i++) {
    servos[i].attach(servoPins[i]);
    servos[i].write(servoPositions[i]); // Set initial position
  }
}

void loop() {
  if (Serial.available() > 0) {
    char receivedByte = Serial.read();
    
    // Determine which servo to move based on the received command
    int servoIndex = receivedByte / 2; // Determine servo index (0-4)
    int position = (receivedByte % 2) * 90; // Determine position (0 or 90 degrees)
    
    if (servoIndex < NUM_SERVOS) {
      servoPositions[servoIndex] = position; // Update position
      servos[servoIndex].write(position); // Move servo to the new position
      Serial.print("Servo ");
      Serial.print(servoIndex);
      Serial.print(" moved to ");
      Serial.println(position);
    }
  }
}
