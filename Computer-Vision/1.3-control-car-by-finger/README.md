# Hand-Controlled Car Using MediaPipe and Arduino

This project demonstrates how to control a car using finger gestures, detected via a webcam, with the help of MediaPipe's hand tracking module. Finger gestures are identified and sent to an Arduino via serial communication to control the movement of a car.

## Features

- Real-time hand tracking and finger detection using MediaPipe
- Control a car by raising or lowering fingers
- Detects which hand (left or right) is used
- Sends control signals to Arduino based on the detected finger positions
- Display live video feed with hand landmarks and bounding boxes

## Components Used

1. **Webcam**: For capturing hand gestures
2. **MediaPipe**: For detecting hand landmarks and tracking finger positions
3. **Arduino**: For receiving serial data and controlling the car
4. **Python Libraries**:
   - `cv2` (OpenCV): For image processing and webcam feed
   - `mediapipe`: For hand tracking and landmark detection
   - `serial`: For serial communication with Arduino
   - `numpy`: For working with hand coordinates
   - `time`: For FPS calculations

## Setup Instructions

### Hardware Requirements
- Arduino with motor drivers and transistors
- Webcam (or external camera)
- USB connection for Arduino
 ### 🚗 Car Components
- **DC Motors**: For driving the car.
- **4 Transistors (2N2222)**: To control the direction of the car (forward and backward).
- **4 LEDs**: Indicate the status and direction of the car.
- **9V Battery**: Power source for the car.- USB connection for Arduino


### Software Requirements
1. Install necessary libraries:
   - `mediapipe`: `pip install mediapipe`
   - `opencv`: `pip install opencv-python`
   - `pyserial`: `pip install pyserial`
   - `numpy`: `pip install numpy`

2. Connect Arduino to your system and upload the corresponding code to handle serial inputs for controlling the car.


### How It Works

1. **Hand Detection**: The webcam captures your hand, and the script uses MediaPipe to detect landmarks (points) on your hand, specifically focusing on your fingers.
2. **Finger Gesture Detection**: The script determines whether a finger is raised or lowered by comparing the y-coordinates of different finger joints.
3. **Sending Control Signals**: Depending on the number of raised fingers, the script sends a corresponding signal to the Arduino via serial communication (`COM4`), which controls the car’s movement.
   - Example:
     - Finger 1 raised → send `0`
     - Finger 2 raised → send `2`
     - Finger lowered → send `1`, `3`, etc.
## Demo 
### Car Before
![car before](https://github.com/user-attachments/assets/305ab637-dcab-4f78-9bcf-2c2eb7ee6356)

### Car After 
![car img](https://github.com/user-attachments/assets/b84b1b3f-10b0-4060-ac26-4fb818eeaecc)

### Demo
https://github.com/user-attachments/assets/440f849d-c8b3-4583-9bc4-ff813598e86d


