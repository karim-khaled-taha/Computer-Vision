import cv2
import mediapipe as mp
import serial
import time
import numpy as np

wCam, hCam = 1200, 720
ptime = 0

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the webcam frame
cap.set(4, 720)   # Set the height of the webcam frame

# Initialize serial communication with Arduino
ser = serial.Serial('COM4', 9600)

# Coordinates for fingertips
finger_Coord_right = [(2, 4), (8, 6), (12, 10), (16, 14), (20, 18)]

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(frame, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Determine if the hand is right or left
                if hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x:
                    hand_side = "left"
                else:
                    hand_side = "Right"
                    # Detect fingers
                    finger_count = 0
                    for finger_idx, (tip_idx1, tip_idx2) in enumerate(finger_Coord_right):
                        tip1_y = hand_landmarks.landmark[tip_idx1].y
                        tip2_y = hand_landmarks.landmark[tip_idx2].y
                        if tip1_y < tip2_y:
                            finger_value = finger_idx * 2
                            finger_count += 1
                        else:
                            finger_value = finger_idx * 2 + 1

                        ser.write(str(finger_value).encode())
                        # print(f'Sent to Arduino: {finger_value}')

                    # Get bounding box coordinates
                    bbox = cv2.boundingRect(np.array([(lm.x * frame.shape[1], lm.y * frame.shape[0]) for lm in hand_landmarks.landmark], dtype=np.int32))
                    x, y, w, h = bbox

                    # Draw bounding box (square)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    # Draw hand landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Print hand side
                    cv2.putText(frame, hand_side, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

                    # Display finger count
                    cv2.putText(frame, f'Fingers: {finger_count}', (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)

        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
ser.close()  # Close the serial communication



########################################################################################################################################################################################

# another method for detecting fingers

# import cv2
# import mediapipe as mp
# import serial
# import time
# import numpy as np

# wCam, hCam = 1200, 720
# ptime = 0

# # Initialize MediaPipe hands module
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# # Initialize webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)  # Set the width of the webcam frame
# cap.set(4, 720)   # Set the height of the webcam frame

# # Initialize serial communication with Arduino
# # ser = serial.Serial('COM4', 9600)

# # Coordinates for fingertips
# finger_Coord_right = [(4, 2), (8, 6), (12, 10), (16, 14), (20, 18)]

# with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
#     while cap.isOpened():
#         success, frame = cap.read()
#         if not success:
#             break

#         frame = cv2.flip(frame, 1)
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = hands.process(rgb_frame)
#         ctime = time.time()
#         fps = 1 / (ctime - ptime)
#         ptime = ctime
#         cv2.putText(frame, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 # Determine if the hand is right or left
#                 if hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x:
#                     hand_side = "left"
#                 else:
#                     hand_side = "right"
#                     finger_state = []
#                     # Detect fingers
#                     for tip_idx1, tip_idx2 in finger_Coord_right:
#                         tip1_y = hand_landmarks.landmark[tip_idx1].y
#                         tip2_y = hand_landmarks.landmark[tip_idx2].y
#                         if tip1_y < tip2_y:
#                             finger_state.append(1)  # Finger is raised
#                         else:
#                             finger_state.append(0)  # Finger is lowered

#                     # Print the finger states array
#                     print(f'Finger states: {finger_state}')

#                     # Check if all fingers are raised
#                     if finger_state == [1, 1, 1, 1, 1]:
#                         print("All fingers are raised!")
#                         # Send specific signal to Arduino
#                         # ser.write(b'11111')

#                     # Convert the finger states array to a string and send to Arduino
#                     finger_state_str = ''.join(map(str, finger_state))
#                     # ser.write(finger_state_str.encode())

#                 # Get bounding box coordinates
#                 bbox = cv2.boundingRect(np.array([(lm.x * frame.shape[1], lm.y * frame.shape[0]) for lm in hand_landmarks.landmark], dtype=np.int32))
#                 x, y, w, h = bbox

#                 # Draw bounding box (square)
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#                 # Draw hand landmarks
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#                 # Print hand side
#                 cv2.putText(frame, hand_side, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)

#         cv2.imshow('Hand Tracking', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()
# # ser.close()  # Close the serial communication

