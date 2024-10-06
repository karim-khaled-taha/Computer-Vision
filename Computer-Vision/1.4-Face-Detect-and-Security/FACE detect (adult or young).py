import cv2
import serial

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the webcam frame
cap.set(4, 720)   # Set the height of the webcam frame

# Initialize serial communication with Arduino
#ser = serial.Serial('COM4', 9600)  # Change 'COM4' to the correct port

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Camera not found or cannot be opened.")
    exit()

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale (face detection works better in grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Filter faces based on size (assuming adult faces are larger)
    adult_faces = []
    for (x, y, w, h) in faces:
        if w > 200 and h > 200:  # Adjust these thresholds as needed
            adult_faces.append((x, y, w, h))

    young_faces = []
    for (x, y, w, h) in faces:
        if w < 200 and h < 200:  # Adjust these thresholds as needed
          young_faces.append((x, y, w, h))        

    # Send the number of adult faces to Arduino only if there are adult faces detected
    #if len(adult_faces) > 0:
      #  ser.write(b'0')
    #else:
     #    ser.write(b'1')


    # Draw rectangles around the detected adult faces
    for (x, y, w, h) in adult_faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "adult", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

    # Draw rectangles around the detected young faces
    for (x, y, w, h) in young_faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "young", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 3)
    

    # Display the frame with detected adult faces
    cv2.imshow('Adult Face Detection', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
