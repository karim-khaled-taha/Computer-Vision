import cv2
import mediapipe as mp
import serial
import time

ptime = 0

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the webcam frame
cap.set(4, 720)   # Set the height of the webcam frame

# Initialize serial communication with Arduino
ser = serial.Serial('COM4', 9600)  # Change 'COM3' to the appropriate port

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(frame, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Calculate the y-coordinate of the thumb tip and index finger tip
                wrist_tip = landmarks.landmark[mp_hands.HandLandmark.WRIST]
                thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_finger_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
                thumb_y = thumb_tip.y
                index_y = index_finger_tip.y
                middle_y = middle_tip.y
                ring_y = ring_tip.y
                pinky_y = pinky_tip.y
                

                # Compare y-coordinates to detect finger raise
                if thumb_y < index_y:
                    ser.write(b'0')  # Sending '1' to Arduino
                else:
                    ser.write(b'1')  # Sending '0' to Arduino

                if thumb_y < middle_y:
                    ser.write(b'3')  # Sending '1' to Arduino
                else:
                    ser.write(b'2')  # Sending '0' to Arduino 

                if thumb_y < ring_y:
                    ser.write(b'5')  # Sending '1' to Arduino
                else:
                    ser.write(b'4')  # Sending '0' to Arduino 

                if thumb_y < pinky_y:
                    ser.write(b'7')  # Sending '1' to Arduino
                else:
                    ser.write(b'6')  # Sending '0' to Arduino  

                



                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
ser.close()  # Close the serial communication
