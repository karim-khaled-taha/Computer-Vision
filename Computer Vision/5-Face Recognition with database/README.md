# Face Recognition System

This project implements a face recognition system using OpenCV, `face_recognition`, and `cvzone` libraries. It detects and recognizes faces from a live webcam feed, estimates their distance from the camera, and identifies known faces based on preloaded encodings.

## Features

- **Face Detection**: Detects faces in real-time using the `cvzone` FaceMesh module.
- **Face Recognition**: Recognizes known faces by comparing their encodings against a database of known faces.
- **Distance Estimation**: Estimates the distance of the detected face from the camera.
- **Face Box Highlighting**: Draws a box around the face and displays the name if the face is recognized.
- **Text-to-Speech (TTS)**: (Not utilized in the current code, but can be added for additional functionality like voice alerts.)

### Code Explanation
## face_recognition_system.py
Initialization:

- The `FaceMeshDetector` from `cvzone` is used to detect facial landmarks.
- The `SimpleFacerec class` is used for loading known face encodings and detecting faces in the frame.

## Simple_Facerec.py
Class SimpleFacerec:
__init__: Initializes lists for storing known face encodings and names.
- **load_encoding_images**: Loads images from the specified path, encodes them, and stores them.
- **detect_known_faces**: Detects faces in the frame, compares them to known faces, and returns the locations and names of recognized faces.

