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


---


### Steps:

## Dataset

To build an accurate fire detection model, you will need a well-labeled dataset. We recommend gathering various fire images under different lighting and environmental conditions.

- **Sample Fire Dataset**: You can download a sample dataset from [[link to dataset](https://universe.roboflow.com/-jwzpw/continuous_fire/dataset/6)](#).


## 1. Google Colab Training

If you don't have a local machine with a GPU, you can train the YOLOv8 model using [Google Colab](https://colab.research.google.com/).

1. Upload your dataset to Google Drive.
2. Open the [[YOLOv8 Fire Detection Colab Notebook](https://colab.research.google.com/drive/1rOrocSNvpBsdsLjyZuOwvhA4ZYy4_qtl#scrollTo=1c6nzoiMOzdE)](#).
3. Follow the instructions to train the model on your dataset.
4. After training, download the trained model (`best.pt`) and place it in the project folder.


