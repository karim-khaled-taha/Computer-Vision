import cv2
from ultralytics import YOLO

# Load the trained model
model = YOLO(r'D:\Application\Projects\14-Parking Management\BY yolo v11 V1.0\best.pt')  # Replace with your custom model path

# Open the video file
video_path = 'carPark.mp4'  # Replace with your video path
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame
    frame = cv2.resize(frame, (700, 800), interpolation=cv2.INTER_AREA)

    # Perform inference on the current frame
    results = model(frame)

    # Initialize counters
    total_parking_spots = 0  # Adjust this based on the actual number of parking spots
    occupied_parking_spots = 0
    parking_spots = 0

    # Extract bounding box coordinates and class names
    for box, cls in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        x1, y1, x2, y2 = map(int, box)  # Convert bounding box coordinates to integers
        obj = model.names[int(cls)]  # Get the name of the detected object

        # Count and draw rectangles based on the object type
        if obj == 'occupied-parking-spots':  # Adjust to match your model's labels
            occupied_parking_spots += 1
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red rectangle for occupied
        elif obj == 'parking spot':  # Adjust to match your model's labels
            parking_spots += 1
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green rectangle for free spots

    # Calculate the total number of parking spots
    total_parking_spots = parking_spots + occupied_parking_spots

    # Display the text annotations on the frame
    cv2.putText(frame, f"Parking free: {parking_spots}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    cv2.putText(frame, f"Occupied parking: {occupied_parking_spots}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    cv2.putText(frame, f"Total parking spots: {total_parking_spots}", (10, 780), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

    
     # Visualize the results
    # annotated_frame = results[0].plot()  # This adds bounding boxes to the frame# Display the frame with rectangles
    
    
    cv2.imshow('Car Park', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
cv2.destroyAllWindows()
