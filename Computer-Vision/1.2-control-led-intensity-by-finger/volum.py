import cv2
import mediapipe as mp
import numpy as np
import time
import serial

ptime = 0

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the webcam frame
cap.set(4, 720)   # Set the height of the webcam frame

ser = serial.Serial('COM4', 9600)  # Adjust COM port and baud rate as necessary

# Coordinates for fingertips
finger_Coord = [(4, 2), (8, 6), (12, 10), (16, 14), (20, 18)]

# Define LED level control variables
min_distance = 0.1  # Minimum normalized distance
max_distance = 1.5  # Maximum normalized distance
min_led_level = 0    # Minimum LED level (e.g., 0%)
max_led_level = 100  # Maximum LED level (e.g., 100%)

def map_value(value, from_min, from_max, to_min, to_max):
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        img_h, img_w, img_c = frame.shape
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(frame, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

        if results.multi_hand_landmarks:
            # Only process the first hand detected
            landmarks = results.multi_hand_landmarks[0]

            # Initialize points for thumb and index finger circles
            thumb_x, thumb_y = int(landmarks.landmark[4].x * img_w), int(landmarks.landmark[4].y * img_h)
            index_x, index_y = int(landmarks.landmark[8].x * img_w), int(landmarks.landmark[8].y * img_h)

            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), cv2.FILLED)  # Circle on thumb top
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)  # Circle on index finger top

            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate multiple reference distances (e.g., wrist to base of each finger)
            wrist_x, wrist_y = int(landmarks.landmark[0].x * img_w), int(landmarks.landmark[0].y * img_h)
            reference_points = [landmarks.landmark[5], landmarks.landmark[9], landmarks.landmark[13], landmarks.landmark[17]]
            reference_distances = [calculate_distance((wrist_x, wrist_y), (int(p.x * img_w), int(p.y * img_h))) for p in reference_points]
            avg_reference_distance = np.mean(reference_distances)

            # Calculate the distance between thumb and index finger
            fingertip_distance = calculate_distance((thumb_x, thumb_y), (index_x, index_y))
            
            # Normalize the fingertip distance by the averaged reference distance
            normalized_distance = fingertip_distance / avg_reference_distance
            
            # Draw a line between the two circles if both points are defined
            cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 0), 2)

            # Map the normalized distance to LED level (adjust the mapping according to your needs)
            led_level = int(map_value(normalized_distance, min_distance, max_distance, min_led_level, max_led_level))

            # Check if fingertips are close together to turn off the LED
            if fingertip_distance <= 25:  # Adjust this threshold as needed
                led_level = 0

            # Send LED level to Arduino
            ser.write(f"L{led_level}\n".encode())

            cv2.circle(frame, ((thumb_x + index_x) // 2, (thumb_y + index_y) // 2), 10, (0, 255, 0), cv2.FILLED)

            # Display the distance, normalized distance, and LED level on the frame
            cv2.putText(frame, f'Distance: {fingertip_distance:.2f} px', (40, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, f'Normalized Distance: {normalized_distance:.2f}', (40, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, f'LED Level: {led_level}%', (40, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Hand Tracking', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
ser.close()
