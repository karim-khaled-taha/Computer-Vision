# Parking Management System

## Overview
This project is a Parking Management System that detects available and occupied parking spaces using image processing and deep learning methods. The system has four versions, each employing different techniques and models for detection.

## Features
- **Version 1:** Uses traditional image processing techniques to detect available parking spots.
- **Version 2:** Utilizes YOLOv5 to detect cars. The camera is placed at a non-top view angle.
- **Version 3:** Leverages YOLOv11, trained on custom data, to identify free and occupied parking spots. The camera is placed on top.
- **Version 4:** Uses YOLOv11, trained with top-view images of cars to better detect cars and parking spaces.

## Version Details

### [Version 1: Image Processing (Top View)](https://github.com/karim-khaled-taha/Computer-Vision/tree/main/Computer-Vision/2.3-Parking_Management/by_image_processing)
- This version uses classical image processing techniques (e.g., edge detection, contouring) to analyze parking lot images.
- **Pros:** Simple and fast.
- **Cons:** Sensitive to lighting and requires fine-tuned parameters.
- [Watch the video](https://github.com/user-attachments/assets/76cfdc0a-7d6f-45c5-b77c-edd1f6447c83)


### [Version 2: YOLOv5 Car Detection (Non-top view)](https://github.com/karim-khaled-taha/Computer-Vision/tree/main/Computer-Vision/2.3-Parking_Management/by_Yolov5)
- YOLOv5 is used to detect cars from a non-top view angle.
- **Pros:** Faster detection of cars.
- **Cons:** Performance may vary with camera angles.
- [Watch the video](https://github.com/user-attachments/assets/aa195183-10b3-497d-92b2-ac23d166d873)



### [Version 3: YOLOv11 Car Detection (Custom Data, Top view)](https://github.com/karim-khaled-taha/Computer-Vision/tree/main/Computer-Vision/2.3-Parking_Management/BY_Yolov11_V1.0)
- YOLOv11 is trained with a dataset that includes free and occupied parking spaces.
- The camera is placed at a non-top view angle.
- **Pros:** Higher accuracy due to customized training data.
- **Cons:** Dataset-specific, may not generalize well to all parking lots.
- [Watch the video](https://github.com/user-attachments/assets/e2331997-a9b9-4468-9eea-b9a300c77f96)



### [Version 4: YOLOv11 Car Detection (Custom Data, Top View)](https://github.com/karim-khaled-taha/Computer-Vision/tree/main/Computer-Vision/2.3-Parking_Management/BY_Yolov11_V2.0)
- YOLOv11 is trained with top-view images of cars and parking spaces.
- **Pros:** Improved detection due to consistent top-view perspective.
- **Cons:** Requires a specific camera placement for optimal results.
- [Watch the video](https://github.com/user-attachments/assets/d97363d3-873c-41ec-a9ec-8f3a3abec53c)



## Dataset
- For **Version 3**, the dataset includes labeled images of free and occupied parking spots, captured from various angles (not top-view).
- For **Version 4**, the dataset consists of top-view images with cars and empty spaces.

## Requirements

### General
- Python 3.x
- OpenCV
- YOLOv5/YOLOv8 (PyTorch)

### Specific Libraries
- Version 1:
  - OpenCV
- Version 2:
  - PyTorch
  - YOLOv5
- Version 3 and 4:
  - PyTorch
  - YOLOv8


