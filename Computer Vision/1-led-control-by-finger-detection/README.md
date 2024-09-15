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
![0](https://github.com/user-attachments/assets/ed1055ba-3803-4dec-935e-09641278eb1f)
![1](https://github.com/user-attachments/assets/308135b9-9cc4-4e21-93f7-8a6ca28fd1d6)
![2](https://github.com/user-attachments/assets/3edcb8b3-50f4-4470-873a-d3e9f4b09882)
![3](https://github.com/user-attachments/assets/36ddbead-0911-4c53-bacf-9e8f0ec455a5)
![4](https://github.com/user-attachments/assets/db14d2b9-e5c5-44ce-a1f4-6f73bd7a83e3)
![5](https://github.com/user-attachments/assets/b0c1e1f7-614f-4e0f-b374-e1f8bf005156)

