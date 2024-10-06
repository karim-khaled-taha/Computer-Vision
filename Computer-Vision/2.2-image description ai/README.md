# AI-Powered Image Description Generator for Blind Users

This project uses OpenCV, Google Generative AI, and PIL to capture images from a webcam and generate descriptive content for blind or visually impaired individuals. The system captures an image when the user presses a specific key and uses an AI model to generate a text description of the image.

## Features
- Capture images using a webcam in real-time.
- Save captured images to a directory.
- Use Google's Generative AI model to generate a textual description of the captured images.
- Save both images and their corresponding descriptions.
- User-friendly key press actions for capturing and exiting.

## How It Works
- **Webcam Capture**: The system continuously captures video from your webcam. 
- **Image Capture**: When the user presses the 'z' key, the current frame is captured, saved, and sent to the AI model to generate a description.
- **AI-Generated Description**: The AI model generates descriptive text, which is saved in a `.txt` file for each image.
- **Real-Time Display**: The live video feed is displayed on the screen, and the user can press the 'ESC' key to exit the program.


### Libraries Used:
- **OpenCV**: Used to capture video and images from the webcam.
- **PIL (Python Imaging Library)**: Used to convert OpenCV images to PIL format for saving.
- **Google Generative AI**: Used to generate text descriptions of images.


## Demo
![image_1](https://github.com/user-attachments/assets/dbc6abe4-573f-4c1a-9b57-6e36277150c6)
 - **The Description**:
     A man with closely shaved hair and a goatee is holding a smartphone to his ear, as if in the middle of a phone call. He's wearing a yellow or mustard-colored shirt.  The background suggests he might be indoors, with part of a window and a light wall visible behind him. He has a neutral expression on his face. 
