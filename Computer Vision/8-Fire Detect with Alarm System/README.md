# Fire Detection System Using YOLOv8 and Arduino

This project aims to create a real-time fire detection system using a trained YOLOv8 model and an Arduino setup for alerts. The system detects fire from a webcam feed and sends signals to an Arduino, which can activate a buzzer or other alert mechanisms.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Training the Model](#training-the-model)
- [Dataset](#dataset)
- [Google Colab Training](#google-colab-training)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

---

## Introduction

Fire detection is critical in various environments, and using computer vision can enhance safety systems. In this project, we utilize the YOLOv8 object detection model to identify fire in a video feed from a camera and communicate the detection to an Arduino for triggering alerts.

---

## Features

- **Real-Time Detection**: Detects fire in live video streams.
- **YOLOv8 Model**: Uses a pre-trained or custom-trained YOLOv8 model for object detection.
- **Arduino Integration**: Sends a signal to an Arduino microcontroller to trigger a buzzer or other alert mechanisms upon detecting fire.
- **Adjustable Confidence Threshold**: You can adjust the detection confidence level.
- **Customizable Alerts**: The Arduino can be programmed to trigger different responses based on detection.

---

## System Architecture

1. **Webcam Feed**: Captures live video frames.
2. **YOLOv8 Model**: Processes the frames to detect fire.
3. **Arduino Communication**: Sends signals to the Arduino based on detection results.
4. **Alert Mechanism**: The Arduino activates a buzzer or any other connected alert system when fire is detected.

![System Architecture](#) *(Placeholder for system architecture diagram)*

---

## Requirements

To run this project, you will need:

- Python 3.x
- OpenCV
- YOLOv8 (Ultralytics)
- PySerial (for Arduino communication)
- Arduino board (with buzzer or other alert system)
- A webcam
- A trained YOLOv8 model

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/fire-detection-yolov8-arduino.git
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that your Arduino is connected to your computer and the correct port is specified in the code.

4. Download the YOLOv8 trained model from the [Model Training section](#training-the-model) or use the pre-trained `best.pt` file.

---

## How It Works

1. **YOLOv8 Inference**: The system uses the YOLOv8 model to analyze the video feed. The model is trained to recognize fire and outputs bounding boxes with confidence scores.
2. **Detection Logic**: If fire is detected with a confidence above the threshold, a signal is sent to the Arduino.
3. **Arduino Communication**: The Arduino receives the signal and triggers the buzzer or other alerts.
4. **Real-Time Display**: The system displays the video feed with detected objects highlighted for easy monitoring.

---

## Training the Model

You can train the YOLOv8 model for fire detection using a custom dataset.

- **Data Collection**: Collect images containing fire and non-fire scenarios. Label them using a tool like LabelImg, and save the annotations in YOLO format.
- **Model Training**: Train the YOLOv8 model using [Google Colab](#google-colab-training) or a local GPU-based system.

---

## Dataset

To build an accurate fire detection model, you will need a well-labeled dataset. We recommend gathering various fire images under different lighting and environmental conditions.

- **Sample Fire Dataset**: You can download a sample dataset from [link to dataset](#).
- **Creating Your Own Dataset**: Capture images from different sources (e.g., security cameras, stock photos) and manually label them using YOLOv8 format.

---

## Google Colab Training

If you don't have a local machine with a GPU, you can train the YOLOv8 model using [Google Colab](https://colab.research.google.com/).

### Steps:

1. Upload your dataset to Google Drive.
2. Open the [YOLOv8 Fire Detection Colab Notebook](#).
3. Follow the instructions to train the model on your dataset.
4. After training, download the trained model (`best.pt`) and place it in the project folder.

---

## Future Improvements

Here are a few ways the system can be expanded and improved:

- **Multi-Hazard Detection**: Extend the model to detect other hazards such as smoke or gas leaks.
- **IoT Integration**: Connect the Arduino to a cloud service for remote monitoring and alerts via mobile devices.
- **Improved Accuracy**: Retrain the model with more diverse datasets to improve fire detection in different environments.
- **Integration with Security Systems**: Incorporate the system into existing building security systems for automated responses (e.g., fire suppression).

---

## Acknowledgments

This project was built using the open-source [YOLOv8 model by Ultralytics](https://github.com/ultralytics/yolov8) and inspired by real-time fire detection needs in safety systems.

We would like to thank [link to contributors] for their contributions and [link to dataset providers] for providing the necessary datasets.

