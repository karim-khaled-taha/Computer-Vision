import cv2
import face_recognition
import os
import time
import serial
import pyttsx3
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

# Initialize FaceMeshDetector
detector = FaceMeshDetector()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize serial communication with Arduino (if needed)
# arduino = serial.Serial('COM4', 9600)  # Replace 'COM4' with the correct port for your Arduino

# Specify the directory containing the images
face_database_path = r"Database v0.3"

# Flag to enable or disable face_recognition library
face_recognition_enabled = True

if face_recognition_enabled:
    # Load the face encodings of the images in the face database folder
    face_encodings = []
    face_names = []
    for filename in os.listdir(face_database_path):   
            file_path = os.path.join(face_database_path, filename)
            try:
                # Load image
                image = face_recognition.load_image_file(file_path)
                
                # Get face encodings
                encodings = face_recognition.face_encodings(image)
                
                if encodings:
                    face_encodings.append(encodings[0])
                    face_names.append(os.path.splitext(filename)[0])
                else:
                    print(f"No faces found in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the webcam frame
cap.set(4, 720)   # Set the height of the webcam frame

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Camera not found or cannot be opened.")
    exit()

ptime = 0

# Define the coordinates of the middle box
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
    # Read a frame from the camera
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    # Draw the middle box
    cv2.rectangle(frame, (box_left, box_top), (box_right, box_bottom), (255, 255, 255), 2)

    # Resize the frame to a smaller size
    resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Convert the resized frame to RGB
    rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    
    frame, face  = detector.findFaceMesh(frame, draw=False)


    if face:
        face = face[0]
        pointLeft = face[145]
        pointRight = face[374]
        # Drawing
        cv2.line(frame, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(frame, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight) # distance between the two eyes in pixels
        # print(w)
        W = 6.3 # constant Width of the face in cm

        # Finding the Focal Length
        # d = 70 # distance in cm from the camera 
        # f = (w * d) / W
        # print(f)

        # Finding distance
        f = 1180
        d = (W * f) / w
        # print(d)

        cvzone.putTextRect(frame, f'Depth: {int(d)}cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)

    if face_recognition_enabled:
        # Find all the faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(frame, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

        face_detected_inside_box = False

        if face_locations:
            for (top, right, bottom, left) in face_locations:
                # Convert face coordinates to match the original frame size
                top *= 2
                right *= 2
                bottom *= 2
                left *= 2

                

                # Check if the face is inside the middle box
                if left > box_left and right < box_right and top > box_top and bottom < box_bottom and d < 100:
                    face_detected_inside_box = True

                    # If face is detected inside the box and not already recognized
                    if not recognized_face_in_box:
                        # Provide audio feedback
                        engine.say("There is someone in front of you, do you want to know him?")
                        engine.runAndWait()

                        # Wait for user input ('M' to accept, 'N' to decline)
                        while True:
                            key = cv2.waitKey(0)
                            if key == ord('m'):
                                # Proceed with face recognition
                                face_encodings_frame = face_recognition.face_encodings(rgb_frame, [(top // 2, right // 2, bottom // 2, left // 2)])
                                for face_encoding in face_encodings_frame:
                                    matches = face_recognition.compare_faces(face_encodings, face_encoding)
                                    recognized_face_name = "Unknown"  # Default name for unrecognized faces
                                    color = (0, 255, 0)  # Default color for recognized faces

                                    # Find the index of the first match
                                    if True in matches:
                                        first_match_index = matches.index(True)
                                        recognized_face_name = face_names[first_match_index]
                                        recognized_face_in_box = True  # Set flag to true as the face is recognized
                                        # arduino.write(b'0\n')  # Send "Match" to Arduino
                                    else:
                                        color = (0, 0, 255)  # Red color for unrecognized faces
                                        recognized_face_in_box = True  # Even unknown faces are considered recognized for this session
                                        # arduino.write(b'1\n')  # Send "Unknown" to Arduino

                                    # Draw a rectangle around the face and display the name
                                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                                    cv2.putText(frame, recognized_face_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                                break  # Break out of the loop to continue processing
                            elif key == ord('n'):
                                # Don't proceed with face recognition
                                recognized_face_in_box = False  # No recognition action
                                break  # Break out of the loop to continue processing
                    else:
                        # Track and display the recognized face without prompting again
                        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                        cv2.putText(frame, recognized_face_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color ,2)
                    
                    break  # Stop checking other faces if one is already detected inside the box

        # If no face is detected inside the box, reset recognition status and send signal to Arduino
        if not face_detected_inside_box:
            if recognized_face_in_box:
                # Face left the box
                # arduino.write(b'3\n')  # Send "NoFace" signal to Arduino
                recognized_face_in_box = False
                recognized_face_name = ""

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
# arduino.close()
