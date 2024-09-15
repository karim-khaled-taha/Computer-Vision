# Hand Gesture-Controlled LED Level using OpenCV and Arduino

This project demonstrates how to control an LED's brightness level based on the distance between your thumb and index finger using computer vision (OpenCV) and an Arduino. It uses MediaPipe to detect hand landmarks and calculate the distance between fingertips, sending this data to an Arduino to control an LED.

## Features
- **Hand Gesture Recognition**: Detects hand landmarks and tracks the position of the thumb and index finger.
- **LED Level Control**: Calculates the distance between the thumb and index finger, maps it to a percentage, and sends the value to the Arduino to adjust the LED brightness.
- **Real-time Processing**: Displays FPS (Frames per Second) and real-time values for fingertip distance and corresponding LED brightness level.

## Requirements

### Hardware:
- Arduino (e.g., Arduino Uno)
- LED and appropriate resistor
- Jumper wires
- USB cable for Arduino
- A computer with a webcam

### Software:
- Python 3.x
- OpenCV
- MediaPipe
- Numpy
- PySerial


## How It Works

- The project utilizes **MediaPipe** to detect hand landmarks.
- The thumb and index finger positions are extracted to calculate their distance.
- This distance is normalized based on the hand size and mapped to a percentage (0–100%).
- The percentage is sent to the Arduino over a serial connection to adjust the LED brightness using **PWM**.

## Demo

[![Hand Gesture Demo](demo.gif)
](https://github.com/user-attachments/assets/aaee18f1-ca01-469d-872b-75d34779133c
)
