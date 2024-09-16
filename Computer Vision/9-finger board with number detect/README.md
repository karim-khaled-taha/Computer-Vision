
# Hand Gesture-Based Drawing and YOLOv8 Number Detection with Arduino Communication

## Overview

This project implements a hand gesture-controlled drawing application using a webcam, Mediapipe for hand tracking, and YOLOv8 for number detection on a drawing window. It also communicates detected numbers to an Arduino via serial communication.

## Features

1. **Hand Gesture Drawing**: 
   - Detect hand gestures to draw on a window using different colors (Blue, Green, Red, Yellow, and Black).
   - Use an eraser function by bringing fingers close together.   
       
2. **Color Selection**:
   - Select from five colors (Blue, Green, Red, Yellow, Black) by moving your hand over the respective color buttons.
   - A "CLEAR" button to reset the drawing.

3. **YOLOv8 Integration**:
   - After drawing a number, the model detects and predicts it in real-time.
   - The prediction is then sent via serial communication to an Arduino.

4. **Arduino Communication**:
   - The detected number is sent to the Arduino, where further actions can be taken based on the number received.

 ### control System By Finger 
   -  **Index Finger**: Acts as the drawing tool, allowing you to sketch with precision.
   - **Index & Middle Finger**: Used to stop the drawing.
   - **Ring Finger**: Activates YOLOv8 mode, to predict the number and send to Arduino.
   - **Lower Thumb & Index & Middle**: Functions as an eraser, enabling you to remove parts of the drawing with ease.

## Demo Project
https://github.com/user-attachments/assets/471a5df4-aa91-4787-9c69-6ec75b9cada7

