import cv2
import numpy as np
import mediapipe as mp
from collections import deque
from ultralytics import YOLO
import serial

arduino = serial.Serial('COM4', 9600)

# Initialize points and colors
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]
ppoints = [deque(maxlen=1024)]

blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0
black_index = 0

eraser_radius = 30

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (0, 0, 0)]
colorIndex = 5

paintWindow = np.ones((640, 640, 3), np.uint8) * 255  # White background

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mpDraw = mp.solutions.drawing_utils

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Load the YOLOv8 model
model = YOLO(r"D:\Application\Projects\10-finger board\best (1).pt")
model_active = False  # Flag to control model prediction state

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Drawing buttons on the frame
    frame = cv2.rectangle(frame, (335, 1), (430, 65), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (450, 1), (545, 65), (255, 0, 0), 2)
    frame = cv2.rectangle(frame, (565, 1), (660, 65), (0, 255, 0), 2)
    frame = cv2.rectangle(frame, (680, 1), (775, 65), (0, 0, 255), 2)
    frame = cv2.rectangle(frame, (795, 1), (890, 65), (0, 255, 255), 2)
    frame = cv2.rectangle(frame, (910, 1), (1005, 65), (0, 0, 0), 2)

    cv2.putText(frame, "CLEAR", (375, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (475, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (588, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (710, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (810, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLACK", (945, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

    # Hand detection and processing
    result = hands.process(framergb)

    finger_Coord_right = [(20, 18)]
    finger_Coord_right0 = [ (8, 6), (12, 10)]

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * 1280)
                lmy = int(lm.y * 720)
                landmarks.append([lmx, lmy])
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Control model prediction state based on pinky finger
            for finger_idx, (tip_idx1, tip_idx2) in enumerate(finger_Coord_right):
                tip1_y = handslms.landmark[tip_idx1].y
                tip2_y = handslms.landmark[tip_idx2].y
                if tip1_y < tip2_y:
                    model_active = True
                else:
                    model_active = False

        thumb_finger = (landmarks[4][0], landmarks[4][1])
        ring_finger = (landmarks[16][0], landmarks[16][1])
        pinky_finger = (landmarks[20][0], landmarks[20][1])
        index_finger = (landmarks[8][0], landmarks[8][1])
        middle_finger = (landmarks[11][0], landmarks[11][1])
        cv2.circle(frame, index_finger, 3, (0, 255, 0), -1)

        
        finger_distance_index_middle = calculate_distance(index_finger, middle_finger)
        finger_distance_index_thumb = calculate_distance(index_finger, thumb_finger)
        finger_distance_middle_thumb = calculate_distance(middle_finger, thumb_finger)
        finger_distance_middle_ring = calculate_distance(middle_finger, ring_finger)
        finger_distance_ring_pinky = calculate_distance(ring_finger, pinky_finger)

        # Calculate the average position (centroid) of the three fingertips
        centroid_x = int((thumb_finger[0] + index_finger[0] + middle_finger[0]) / 3)
        centroid_y = int((thumb_finger[1] + index_finger[1] + middle_finger[1]) / 3)

        centroid = (centroid_x, centroid_y)


        if abs(finger_distance_index_thumb) < 80 and abs(finger_distance_middle_thumb) < 80 and abs(finger_distance_index_middle) < 80:
              for finger_idx, (tip_idx1, tip_idx2) in enumerate(finger_Coord_right0):
                tip1_y = handslms.landmark[tip_idx1].y
                tip2_y = handslms.landmark[tip_idx2].y
                if tip1_y < tip2_y:
             
                    cv2.circle(frame, centroid, eraser_radius, (0, 0, 0), -1) 

                    
                    # Use the color indices to draw on the frame and paintWindow
                    for idx, points_list in enumerate([bpoints, gpoints, rpoints, ypoints, ppoints]):
                        current_color = colors[idx]
                        
                        for points in points_list:
                            if len(points) < 2:  # Ensure there are at least two points to draw a line
                                continue
                            for i in range(1, len(points)):
                                if points[i - 1] is None or points[i] is None:
                                    continue
                                line_start = points[i - 1]
                                line_end = points[i]
                                
                                # Erase on the frame
                                if calculate_distance(line_start, centroid) < eraser_radius:
                                    cv2.line(frame, line_start, line_end, (255, 255, 255), 20)
                                
                                # Erase on the paintWindow
                                if calculate_distance(line_start, centroid) < eraser_radius:
                                    cv2.line(paintWindow, line_start, line_end, (255, 255, 255), 20)
                                    
                                    # Check if the entire line segment is within the eraser radius
                                    if calculate_distance(line_end, centroid) < eraser_radius:
                                        points.clear()  # Clear the points to erase the line completely
                                        paintWindow[67:, :] = 255
                                        break  # Break to avoid processing cleared points   

        elif abs(finger_distance_index_middle) < 45:
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1
            ppoints.append(deque(maxlen=512))
            black_index += 1

        elif index_finger[1] <= 65:
            if 335 <= index_finger[0] <= 430:
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                ppoints = [deque(maxlen=512)]
                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                black_index = 0
                paintWindow[67:, :] = 255
            elif 450 <= index_finger[0] <= 545:
                colorIndex = 0
            elif 565 <= index_finger[0] <= 660:
                colorIndex = 1
            elif 680 <= index_finger[0] <= 775:
                colorIndex = 2
            elif 795 <= index_finger[0] <= 890:
                colorIndex = 3
            elif 910 <= index_finger[0] <= 1005:
                colorIndex = 4

        else:
            if colorIndex == 0:
                bpoints[blue_index].appendleft(index_finger)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(index_finger)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(index_finger)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(index_finger)
            elif colorIndex == 4:
                ppoints[black_index].appendleft(index_finger)
            elif colorIndex == 5:
                pass  # Do nothing

    else:
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1
        ppoints.append(deque(maxlen=512))
        black_index += 1

    points = [bpoints, gpoints, rpoints, ypoints, ppoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 3)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 3)

    if model_active:
        # Apply YOLOv8 model on the paintWindow and display the predictions
        results = model(paintWindow, conf=0.6)
        prediction = results[0].plot()  # Annotated image with predictions

        cv2.imshow("Paint", prediction)
        detected_numbers = [int(model.names[int(c)]) for c in results[0].boxes.cls]
        print("Detected numbers:", detected_numbers)  # Debugging print

        if detected_numbers:
            number_to_send = detected_numbers[0]  # Take the first detected number
            arduino.write(str(number_to_send).encode())  # Send the number to Arduino
            print(f"Sent '{number_to_send}' to Arduino")  # Debugging print

    else:
     cv2.imshow("Paint", paintWindow)
     cv2.imshow("Frame", frame)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

