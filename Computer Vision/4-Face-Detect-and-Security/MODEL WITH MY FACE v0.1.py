import cv2
import face_recognition
import os
import time
import serial

# Initialize serial communication with Arduino (uncomment if you're using Arduino)
# arduino = serial.Serial('COM4', 9600)  # Replace 'COM4' with the correct port for your Arduino

# Specify the directory containing the images
face_database_path = r"G:\My Drive\id"

# Flag to enable or disable face_recognition library
face_recognition_enabled = True

if face_recognition_enabled:
    # Load the face encodings of the images in the face database folder
    face_encodings = []
    face_names = []
    for filename in os.listdir(face_database_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
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
box_width, box_height = 400, 400
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
box_left = (frame_width - box_width) // 2
box_top = (frame_height - box_height) // 2
box_right = box_left + box_width
box_bottom = box_top + box_height

# Known width of a human face (in cm) for distance estimation
known_face_width_cm = 14  # Average width of an adult face

# Focal length of the camera (you may need to calibrate this)
focal_length = 1000  # Focal length in pixels (calibration needed)

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

                # Calculate face width in pixels
                face_width_pixels = right - left

                # Calculate distance from camera (distance = (known face width * focal length) / face width in pixels)
                distance_cm = (known_face_width_cm * focal_length) / face_width_pixels

                # Check if the face is inside the middle box
                if left > box_left and right < box_right and top > box_top and bottom < box_bottom and distance_cm < 65:
                    face_detected_inside_box = True

                    # Get face encodings within the box
                    face_encodings_frame = face_recognition.face_encodings(rgb_frame, [(top // 2, right // 2, bottom // 2, left // 2)])
                    for face_encoding in face_encodings_frame:
                        # Print the encoding (truncated for readability)
                        print("Current face encoding")
                        # print([round(val, 2) for val in face_encoding[:10]])  # Printing only the first 10 values for brevity

                    for face_encoding in face_encodings_frame:
                        # Compare the face encoding with the face encodings in the database
                        matches = face_recognition.compare_faces(face_encodings, face_encoding)
                        name = "Unknown"  # Default name for unrecognized faces
                        color = (0, 255, 0)  # Default color for recognized faces

                        # Find the index of the first match
                        if True in matches:
                            first_match_index = matches.index(True)
                            name = face_names[first_match_index]
                            # arduino.write(b'0\n')  # Send "Match" to Arduino
                        else:
                            color = (0, 0, 255)  # Red color for unrecognized faces
                            # arduino.write(b'1\n')  # Send "Unknown" to Arduino

                        # Draw a rectangle around the face and display the name
                        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        # else:
            # If no face is detected, send "NoFace" to Arduino
            # arduino.write(b'3\n')
    # else:
        # If the face_recognition library is disabled, send "3" to Arduino
        # arduino.write(b'3\n')

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
# arduino.close()
