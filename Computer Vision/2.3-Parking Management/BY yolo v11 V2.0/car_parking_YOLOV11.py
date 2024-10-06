import cv2
from ultralytics import YOLO
import numpy as np

# Load the trained model
model = YOLO(r'D:\Application\Projects\YOLO\best(1).pt')  # Replace with your custom model path

# Open the video file
video_path = 'carPark.mp4'  # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Define areas of interest (as polygons)
area1 = [(242, 90), (43, 95), (37, 666), (261, 662)]
area2 = [(394, 82), (409, 664), (616, 667), (620, 92)]
area3 = [(748, 81), (857, 83), (870, 655), (747, 671)]
area4 = [(897, 139), (1010, 138), (995, 652), (910, 652)]

while cap.isOpened():
    # Reset video to start if it reaches the end
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the current frame
    results = model(frame)

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
                # Check if center point is within any area of interest
                results1 = cv2.pointPolygonTest(np.array(area1, np.int32), (cx, cy), False)
                results2 = cv2.pointPolygonTest(np.array(area2, np.int32), (cx, cy), False)
                results3 = cv2.pointPolygonTest(np.array(area3, np.int32), (cx, cy), False)
                results4 = cv2.pointPolygonTest(np.array(area4, np.int32), (cx, cy), False)

                # If the car is in one of the areas, track it
                if results1 >= 0 or results2 >= 0 or results3 >= 0 or results4 >= 0:
                    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0 , 225), 2)
                    cv2.putText(frame,str(name),(x1,y1),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),1)

                    points.append([cx])

    # Count cars
    car_count = len(points)
    # print(car_count)
    
    # Draw areas of interest on the frame
    cv2.polylines(frame, [np.array(area1, np.int32)], True, (0, 255, 0), 2)
    cv2.polylines(frame, [np.array(area2, np.int32)], True, (0, 255, 0), 2)
    cv2.polylines(frame, [np.array(area3, np.int32)], True, (0, 255, 0), 2)
    cv2.polylines(frame, [np.array(area4, np.int32)], True, (0, 255, 0), 2)
    cv2.putText(frame, 'Number of cars in parking = ' + str(car_count), (58, 45), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    # Display the frame without annotations
    cv2.imshow('Car Park', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()



