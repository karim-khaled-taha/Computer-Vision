# Hand Tracking and Finger Detection using MediaPipe and Arduino

This project uses **OpenCV** and **MediaPipe** to track hand movements and detect fingers. It also interfaces with an **Arduino** using **serial communication** to send finger-related data. The code can detect both right and left hands and uses the fingertips' coordinates to determine the number of raised fingers.

## Features
- **Hand Detection**: Identifies both right and left hands.
- **Finger Detection**: Counts the number of raised fingers on the right hand.
- **FPS Counter**: Displays the frames per second for tracking performance.
- **Bounding Box**: Displays a bounding box around the detected hand.
- **Arduino Communication**: Sends finger state data to an Arduino over a serial connection.


### Code Overview

1. **Webcam Initialization**:
   The webcam is initialized using OpenCV, and the frame dimensions are set to 1280x720 pixels.
   
2. **MediaPipe Hands Module**:
   The `mp.solutions.hands` module is used to detect hands in the video feed and track finger landmarks. 

3. **Finger Detection**:
   The code tracks the position of each finger using the landmarks provided by MediaPipe. It checks whether the fingertip is higher than the corresponding joint to determine if the finger is raised.

4. **Arduino Communication**:
   The detected finger values are sent to the Arduino using serial communication. Make sure the correct COM port is set.

5. **Bounding Box**:
   A green bounding box is drawn around the detected hand, providing visual feedback on the hand tracking.

### How it Works

- **Hand Detection**: The program uses the MediaPipe Hands solution to detect the wrist and fingertips.
- **Finger Detection Logic**: For each finger, the program compares the y-coordinates of the tip and the base of the finger. If the tip is higher (in the webcam frame), the finger is considered raised.
- **Sending Data to Arduino**: The number corresponding to the detected finger state is sent to the Arduino via serial communication. You can customize how the Arduino reacts to this data.


### Demo
![Screenshot 2024-09-11 174044](https://github.com/user-attachments/assets/48de5c4d-869f-4433-8ea8-34c98c7086a8)
![Screenshot 2024-09-11 173908](https://github.com/user-attachments/assets/bb5c777f-cd53-4d69-9f4f-1932147520a1)
![Screenshot 2024-09-11 173957](https://github.com/user-attachments/assets/183b7e7b-a59c-457c-acd1-d92e1822ab3d)
![Screenshot 2024-09-11 174012](https://github.com/user-attachments/assets/18f9fd4d-ee47-40f3-a2b5-8b9735780a84)
![Screenshot 2024-09-11 174021](https://github.com/user-attachments/assets/af57e5f1-a64f-4054-b925-e89124801747)
![Screenshot 2024-09-11 174034](https://github.com/user-attachments/assets/c3970960-4a54-4318-bfdc-40cf3663048b)
