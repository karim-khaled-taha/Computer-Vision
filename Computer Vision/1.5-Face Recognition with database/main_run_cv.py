import cv2
import time
import pyttsx3
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from Simple_Facerec import SimpleFacerec  # Import the class

# Initialize FaceMeshDetector and SimpleFacerec class
detector = FaceMeshDetector()
sfr = SimpleFacerec()

# Load face encodings from the "Database" folder
face_database_path = "DataBase"
sfr.load_encoding_images(face_database_path)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Camera not found or cannot be opened.")
    exit()

ptime = 0

# Define middle box coordinates
box_width, box_height = 450, 450
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
box_left = (frame_width - box_width) // 2
box_top = (frame_height - box_height) // 2
box_right = box_left + box_width
box_bottom = box_top + box_height

# Variables to track face recognition status
recognized_face_in_box = False
recognized_face_name = ""

while True:
    # Read frame from the camera
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Draw the middle box
    cv2.rectangle(frame, (box_left, box_top), (box_right, box_bottom), (255, 255, 255), 2)

    # Resize the frame for faster processing
    resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Detect the face mesh
    frame, face = detector.findFaceMesh(frame, draw=False)

    if face:
        face = face[0]
        pointLeft = face[145]
        pointRight = face[374]
        cv2.line(frame, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(frame, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)

        W = 11.4  # Real width
        d = 70  # Estimated distance in cm
        f = 700  # Focal length
        d = (W * f) / w  # Calculated distance
        cvzone.putTextRect(frame, f'Depth: {int(d)}cm', (face[10][0] - 100, face[10][1] - 50), scale=2)

    # Detect known faces in the frame
    face_locations, face_names = sfr.detect_known_faces(frame)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        
        

        # Check if the face is inside the middle box
        if left > box_left and right < box_right and top > box_top and bottom < box_bottom and d < 100:
            if not recognized_face_in_box:
                recognized_face_in_box = True
            cv2.putText(frame, f"Face in box: {name}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            # Draw rectangle around the face and display name
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
