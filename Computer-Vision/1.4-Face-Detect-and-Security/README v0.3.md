
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

   
   Focal Length (f) = eyes Width in Image(w) * Known Distance(d) / Known eyes Width(W)
   
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


