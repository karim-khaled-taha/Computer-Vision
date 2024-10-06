# AI-Powered Hand Gesture-Based Drawing & Answering Application

This project is a **hand-gesture based drawing** tool that utilizes **computer vision** and **AI** to allow users to interact with the canvas by drawing with their fingers and erasing content using hand gestures. The application also integrates **Generative AI (LLM)** to solve or interpret drawings and provides responses based on the detected input.

## Features

- **Real-time hand tracking** using the MediaPipe library.
- **Draw and erase** using hand gestures, allowing a smooth, touch-free experience.
- **Dynamic canvas** that supports multiple colors for drawing, and an eraser function when fingers are close.
- Integration with **Generative AI** for content prediction and interpretation:
  - Solve mathematical problems by drawing them on the canvas.
  - Guess or interpret drawings based on user input.
- **Run the application using Streamlit** For Easy Interface User.

## Tech Stack

- **OpenCV**: For handling video capture and image processing.
- **MediaPipe**: For hand detection and gesture recognition.
- **NumPy**: For numerical computations and array operations.
- **Google Generative AI**: To provide AI-based responses.
- **Streamlit**: For creating the interactive web interface.
- **Pillow (PIL)**: For handling images in the app.

## How It Works

1. **Hand Tracking**: The application uses MediaPipe to detect hand landmarks and gestures. It tracks finger movements and calculates distances between key points to determine whether to draw or erase.
   
2. **Gesture-Based Drawing**: Users can draw lines in different colors by moving their index finger across the screen. The thumb gesture controls the AI-powered content generation based on the drawn image.

3. **AI Integration**: 
   - When the pinky finger gesture is detected, the AI model tries to solve a math problem.
   - When the thumb gesture is detected, the AI guesses the drawing.

4. **Dynamic Erasing**: If fingers are closed together, the system interprets this as an erasing action and removes content from the canvas within a certain radius.

## Demo project 
https://github.com/user-attachments/assets/43ee1124-06eb-415b-a7c1-40be19b950cf


