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

# Face Recognition Security V0.3

## New in Version 0.3
- **Distance Check for Face Detection**: 
  The system now includes a distance check, ensuring that only faces detected within a certain distance from the camera are considered for recognition. This adds another layer of security, preventing face recognition attempts from far distances.
- **Enhanced Face Recognition Accuracy**: 
  Fine-tuned the face detection process by incorporating distance measurement, making the recognition process more reliable for individuals standing within a defined range.

### How Distance is Calculated

In this project, the distance from the camera to a detected face is estimated using the **apparent size of the face** in the image. The method is based on the **pin-hole camera model**, which allows us to estimate distance by comparing the known size of an object (in this case, a human face) with its size in the image captured by the camera.
- use The `FaceMeshDetector` from `cvzone` is used to detect facial landmarks for eyes ,this distance The average adult pupillary distance is about 63 mm.

#### Formula Used:
![Screenshot 2024-09-04 085135](https://github.com/user-attachments/assets/d43f0eed-3876-4155-aef0-b8db1259882e)
Where:
- **Known eyes Width (W)**: The Constant width of a eyse face (around 63 mm).
- **Focal Length (f)**: A camera-specific value calculated during the initial calibration phase.
- **eyes Width in Image (w)**: The width of the detected eyes in pixels in the video feed.

#### Steps for Distance Calculation:

1. **Calibration**: First, the camera's **focal length** needs to be calculated by capturing an image of a eyes at a known distance and measuring the eyes width in pixels. The formula for calculating the focal length is:

   
   Focal Length (f) = eyes Width in Image * Known Distance(d) / Known eyes Width(W)
   
![Screenshot 2024-09-15 185202](https://github.com/user-attachments/assets/41dbc431-3a13-4a85-80b1-814e3a441ed5)


   This calibration process is done once, as the focal length is constant for the camera setup.

2. **Real-Time Distance Estimation**:
   - The system detects a eyes and measures the **eyes width in pixels** from the real-time video feed.
   - Using the face width and the pre-calculated focal length, the distance is estimated using the formula .
Distance = (Known Face Width * Focal Length) / Face Width in Image

![Screenshot 2024-09-15 185211](https://github.com/user-attachments/assets/77665124-028e-45b3-aaa4-b973f0a1eb16)


### Demo 
- **when face distance d >100**
![Screenshot 2024-09-15 162536](https://github.com/user-attachments/assets/08a90190-70a5-4421-a214-173a95f1e110)

- **when face distance d <100**
![Screenshot 2024-09-15 162554](https://github.com/user-attachments/assets/801fbf12-568f-45d0-893a-557f72fc15d4)


