# Fire Detection System Using YOLOv8 and Arduino

This project aims to create a real-time fire detection system using a trained YOLOv8 model and an Arduino setup for alerts. The system detects fire from a webcam feed and sends signals to an Arduino, which can activate a buzzer or other alert mechanisms.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Steps](#Steps)

---

## Features

- **Real-Time Detection**: Detects fire in live video streams.
- **YOLOv8 Model**: Uses a pre-trained or custom-trained YOLOv8 model for object detection.
- **Arduino Integration**: Sends a signal to an Arduino microcontroller to trigger a buzzer or other alert mechanisms upon detecting fire.
- **Adjustable Confidence Threshold**: You can adjust the detection confidence level.
- **Customizable Alerts**: The Arduino can be programmed to trigger different responses based on detection.
---

## Requirements

To run this project, you will need:

- Python 3.x
- OpenCV
- YOLOv8 (Ultralytics)
- PySerial (for Arduino communication)
- Arduino board (with buzzer or other alert system)
- A webcam

---

## How It Works

1. **YOLOv8 Inference**: The system uses the YOLOv8 model to analyze the video feed. The model is trained to recognize fire and outputs bounding boxes with confidence scores.
2. **Detection Logic**: If fire is detected with a confidence above the threshold, a signal is sent to the Arduino.
3. **Arduino Communication**: The Arduino receives the signal and triggers the buzzer or other alerts.
4. **Real-Time Display**: The system displays the video feed with detected objects highlighted for easy monitoring.
---


## Steps:

## 1. Dataset

To build an accurate fire detection model, you will need a well-labeled dataset. We recommend gathering various fire images under different lighting and environmental conditions.

- **Sample Fire Dataset**: You can download a sample dataset from [[link to dataset](https://universe.roboflow.com/-jwzpw/continuous_fire/dataset/6)](#).


## 2. Training on Google Colab 


1. Upload your dataset to Google Drive.
2. Open the [[YOLOv8 Fire Detection Colab Notebook](https://colab.research.google.com/drive/1rOrocSNvpBsdsLjyZuOwvhA4ZYy4_qtl#scrollTo=1c6nzoiMOzdE)](#).
3. Follow the instructions to train the model on your dataset.
4. After training, download the trained model (`best.pt`) and place it in the project folder.


