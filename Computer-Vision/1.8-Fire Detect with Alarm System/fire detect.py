import cv2
import serial
import time
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO(r"D:\Application\Projects\9-model to detect the fire\best.pt")

# Open the web camera
cap = cv2.VideoCapture(0)

# Set the desired width and height for the resized frames
desired_width = 840
desired_height = 640

# Set up serial communication with Arduino
# arduino = serial.Serial('COM4', 9600)  # Update 'COM3' to the correct port for your Arduino
time.sleep(2)  # Wait for the connection to establish

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
        results = model(flipped_frame, conf=0.4)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Check for detections and send data to Arduino
        detected_objects = [model.names[int(c)] for c in results[0].boxes.cls]
        print("Detected objects:", detected_objects)  # Debugging print

        if 'fire' in detected_objects:
            # arduino.write(b'1')  # Send signal to Arduino to turn on the buzzer
            print("Sent '1' to Arduino")  # Debugging print
        else:
            # arduino.write(b'0')  # Send signal to turn off the buzzer
            print("Sent '0' to Arduino")  # Debugging print



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
#arduino.close()
