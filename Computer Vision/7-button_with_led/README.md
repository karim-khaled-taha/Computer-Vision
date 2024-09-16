# Button Control System With Led

## Overview

This project leverages the MediaPipe library for hand tracking and OpenCV for image processing to create an interactive button control system. Using a webcam, the system detects hand gestures and distances between fingers to controll leds. The application communicates with an Arduino via serial communication to send commands based on detected gestures.

## Features

- **Hand Tracking**: Detects hand landmarks and tracks thumb and index finger positions.
- **Distance Measurement**: Measures the distance between the thumb and index finger to perform specific actions.
- **Button Control**: Virtual buttons are drawn on the screen, and actions are triggered when the thumb, index finger, and midpoint are within these button areas.
- **Serial Communication**: Sends commands to an Arduino based on detected gestures.

## Interact with the buttons:

- **Green Button (G)**: Press by positioning your thumb and index finger within the green button area and maintaining a distance of less than 2 cm.
- **Red Button (R)**: Press by positioning your thumb and index finger within the red button area and maintaining a distance of less than 2 cm.
- **Blue Button (B)**: Press by positioning your thumb and index finger within the blue button area and maintaining a distance of less than 2 cm.
