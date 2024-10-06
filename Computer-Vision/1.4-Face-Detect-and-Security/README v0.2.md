# Face Recognition Security System with Sound Feedback, LED, and Buzzer Alerts V0.2

## Overview
This project is a **face recognition-based security system** that integrates **Google Drive** for storing and accessing a face image database. It uses a webcam to detect and recognize faces and provides audio feedback through a text-to-speech engine. Additionally, the system can be connected to an Arduino to control **LEDs and buzzers** for security alerts, notifying the user of recognized or unrecognized faces. 
## Features
- **Face recognition** using `face_recognition` library.
- **Webcam integration** for real-time video feed and face detection.
- **Google Drive integration** for storing face image databases.
- **Dynamic Region of Interest**:
A middle box is drawn on the screen to define the region of interest. Only faces within this box for recognition.
- **Text-to-Speech (TTS)** audio feedback for interaction with the user.
- **LED and Buzzer alerts** via Arduino for security notifications.
- **Interactive interface** to confirm or reject face recognition.
- **Serial communication** between Python and Arduino for controlling hardware components.

## System Components

### Software
- **Python**: Face recognition, image processing, and user interaction.
- **Arduino (optional)**: Hardware alerts using LEDs and a buzzer.
- **Google Drive Setup**:
Store all face images in a directory on Google Drive (e.g., G:\My Drive\id).
Images should be named appropriately (e.g., john_doe.jpg) for easy identification.

### Hardware
- **Webcam**: For capturing live video feed.
- **Arduino**: To control external components (LEDs and buzzer).
- **LEDs** and **Buzzer**: Security indicators for recognized or unrecognized faces.
  
### How It Works
- **Face Detection**: The system captures video from the webcam and detects faces in real time.
- **Face Recognition**: It compares detected faces with the images stored in Google Drive.
- **User Interaction**: When a face is detected within a the medlle Box, the system prompts the user to decide whether to recognize the face (press M for yes, N for no).
- **Hardware Alerts**: If connected, the Arduino will activate an LED for recognized faces and trigger a buzzer for unrecognized faces.
- **Audio Feedback**: The system uses pyttsx3 for text-to-speech feedback to notify the user of recognition events.
### Demo Video
https://github.com/user-attachments/assets/6a6a9a31-33bf-45f9-975d-3aea394a1944

