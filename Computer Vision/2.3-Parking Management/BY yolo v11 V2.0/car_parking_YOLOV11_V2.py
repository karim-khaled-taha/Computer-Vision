import cv2
from ultralytics import YOLO
import numpy as np
import pickle

# Load the trained model
model = YOLO(r'best(1).pt')  # Replace with your custom model path

# Open the video file
video_path = 'carPark.mp4'  # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Define areas of interest (as polygons)
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48

while cap.isOpened():
    # Reset video to start if it reaches the end
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the current frame
    results = model(frame)
    occupied_positions = set()  # Set to keep track of occupied parking spaces


    points = []
    for result in results:  # Loop over results for each detection
        boxes = result.boxes  # Get the bounding boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Convert bounding box coordinates to integers
            label = box.cls  # Class index
            confidence = box.conf  # Confidence score
            name = model.names[int(label)]  # Get the class name

            # Calculate center point of the bounding box
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            if 'Car_Topview' in name:  # Check for car detection
                # Check if the center point is within any area of interest
                for pos in posList:
                    px, py = pos
                    if px < cx < px + width and py < cy < py + height:
                        # If the car is in one of the areas, track it
                        cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)  # Draw center point
                        # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 225), 2)  # Draw bounding box
                        # cv2.putText(frame, str(name), (x1, y1), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)  # Label
                        
                        # Add a red region around the detected car in the parking space
                        cv2.rectangle(frame, (px, py), (px + width, py + height), (0, 0, 255), 2)  # Red region

                        points.append([cx])  # Add center point to list
                        occupied_positions.add(pos)  # Mark this position as occupied
                        break  # Break after finding the first matching parking space


       
     # Count empty parking spaces
    empty_count = 0
    for pos in posList:
        if pos not in occupied_positions:
            empty_count += 1  # Increment if the position is not occupied
            x, y = pos
            cv2.rectangle(frame, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 2)  # Green region for free parking spaces

    car_count = len(points)
    cv2.putText(frame, f'Empty Parking Spaces: {empty_count}/{len(posList)}', (58, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


    # # Draw rectangles for each parking space
    # for pos in posList:
    #     x, y = pos
    #     cv2.rectangle(frame, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 2)  # Green rectangle for parking spaces

    # Display the frame with parking spaces marked
    cv2.imshow('Car Park', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
