import cv2
import serial
import time
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO(r"D:\Application\Projects\10-finger board\best (1).pt")

# Open the web camera
cap = cv2.VideoCapture(1)

# Set the desired width and height for the resized frames
desired_width = 1080
desired_height = 740

# Set up serial communication with Arduino

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Resize the frame
        resized_frame = cv2.resize(frame, (desired_width, desired_height))

        # Flip the frame (1 for horizontal flipping)
        flipped_frame = cv2.flip(resized_frame, 1)

        # Run YOLOv8 inference on the frame
        results = model(frame, conf=0.7)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()


        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
# #####################################################################################################################################
# import cv2
# from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO(r"D:\Application\Projects\10-finger board\best.pt")

# # Load the image
# image_path = r"D:\Application\Projects\10-finger board\Screenshot 2024-07-23 162315.png"
# image = cv2.imread(image_path)

# # Check if the image was loaded successfully
# if image is None:
#     print("Error: Image not loaded.")
# else:
#     # Set the desired width and height for the resized image
#     desired_width = 640
#     desired_height = 640

#     # Resize the image
#     resized_image = cv2.resize(image, (desired_width, desired_height))

#     # Flip the image (1 for horizontal flipping)
#     flipped_image = cv2.flip(resized_image, 1)

#     # Run YOLOv8 inference on the image
#     results = model(resized_image, conf=0.2)

#     # Visualize the results on the image
#     annotated_image = results[0].plot()

#     # Display the annotated image
#     cv2.imshow("YOLOv8 Inference", annotated_image)

#     # Wait for a key press to close the display window
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# ####################################################################################################################################
