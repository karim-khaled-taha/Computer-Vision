import cv2
import mediapipe as mp
import numpy as np
import time

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the webcam frame
cap.set(4, 720)   # Set the height of the webcam frame

ptime = 0

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        img_h, img_w, img_c = frame.shape
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        thumb_x, thumb_y = None, None
        index_x, index_y = None, None

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                thumb_x, thumb_y = int(landmarks.landmark[4].x * img_w), int(landmarks.landmark[4].y * img_h)
                index_x, index_y = int(landmarks.landmark[8].x * img_w), int(landmarks.landmark[8].y * img_h)

                cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), cv2.FILLED)
                cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)

                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        if thumb_x is not None and index_x is not None:
            cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 0), 2)
            distance_in_pixels = np.sqrt((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2)
            cv2.putText(frame, f'Distance: {distance_in_pixels:.2f} px', (40, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(frame, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
