import cv2
import mediapipe as mp
import serial
import time
import numpy as np

ptime = 0
# Initialize flag for buttons 
button1_pressed = False
button2_pressed = False 
button3_pressed = False

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the webcam frame
cap.set(4, 720)   # Set the height of the webcam frame

# Initialize serial communication with Arduino
ser = serial.Serial('COM4', 9600)

# Known real-world distance and its corresponding pixel distance
real_distance_cm = 5  # e.g., 5 centimeters
pixel_distance = 100  # e.g., 50 pixels

# Calculate the conversion factor from pixels to centimeters
conversion_factor = real_distance_cm / pixel_distance


def is_within_button(thumb_x, thumb_y, index_x, index_y, midpoint_x, midpoint_y, button): 
    """
    Checks if the given points (thumb, index, and midpoint) are all within the given button's bounding box.
    
    Parameters
    ----------
    thumb_x : int
        x-coordinate of the thumb
    thumb_y : int
        y-coordinate of the thumb
    index_x : int
        x-coordinate of the index finger
    index_y : int
        y-coordinate of the index finger
    midpoint_x : int
        x-coordinate of the midpoint between the thumb and index finger
    midpoint_y : int
        y-coordinate of the midpoint between the thumb and index finger
    button : tuple of two tuples
        The bounding box of the button as a tuple of two tuples (top-left and bottom-right coordinates)
    
    Returns
    -------
    bool
        True if the points are all within the button's bounding box, False otherwise
    """
    return (
        button[0][0] < thumb_x < button[1][0] and button[0][1] < thumb_y < button[1][1] and
        button[0][0] < index_x < button[1][0] and button[0][1] < index_y < button[1][1] and
        button[0][0] < midpoint_x < button[1][0] and button[0][1] < midpoint_y < button[1][1]
    )

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands: # Initialize MediaPipe hands module
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

        # Initialize points for thumb and index finger circles
        thumb_x, thumb_y = None, None
        index_x, index_y = None, None

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Add circles on the top of the thumb and index finger
                thumb_x, thumb_y = int(landmarks.landmark[4].x * img_w), int(landmarks.landmark[4].y * img_h)
                index_x, index_y = int(landmarks.landmark[8].x * img_w), int(landmarks.landmark[8].y * img_h)

                cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), cv2.FILLED)  # Circle on thumb top
                cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)  # Circle on index  top

                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS) 

        # Draw a line between the two circles if both points are defined 
        if thumb_x is not None and index_x is not None:
            cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 0), 2)
            
            # Calculate the distance between the two points in pixels
            distance_in_pixels = np.sqrt((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) 
            
            # Convert the distance to centimeters
            distance_in_cm = distance_in_pixels * conversion_factor

            # Draw a circle on the midpoint between the two points
            midpoint_x = (thumb_x + index_x) // 2
            midpoint_y = (thumb_y + index_y) // 2
            cv2.circle(frame, (midpoint_x, midpoint_y), 10, (0, 255, 0), cv2.FILLED)
            
            # Display the distance on the frame
            cv2.putText(frame, f'Distance: {distance_in_cm:.2f} cm', (40, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Get frame dimensions 
            height, width, _ = frame.shape

            # Define the dimensions of the buttons
            button_width = 100
            button_height = 100
            button_y = height - button_height - 100  # Position the buttons near the bottom of the frame

            # Calculate the x-coordinate for each button to place them in the middle
            button1_x = (width // 2) - (button_width + 100)
            button2_x = width // 2
            button3_x = (width // 2) + (button_width + 100)

            # Define the coordinates of the buttons
            button1 = [(button1_x, button_y), (button1_x + button_width, button_y + button_height)]
            button2 = [(button2_x, button_y), (button2_x + button_width, button_y + button_height)]
            button3 = [(button3_x, button_y), (button3_x + button_width, button_y + button_height)]

            # Draw the buttons (without filling)
            cv2.rectangle(frame, button1[0], button1[1], (0, 255, 0), thickness=2)  # Green rectangle for button 1
            cv2.rectangle(frame, button2[0], button2[1], (0, 0, 255), thickness=2)  # Red rectangle for button 2
            cv2.rectangle(frame, button3[0], button3[1], (255, 0, 0), thickness=2)  # Blue rectangle for button 3
            
            # Write text in the middle of each rectangle
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]  # Text colors
            # Write "G" in the middle of the first rectangle
            text_size = cv2.getTextSize('G', font, 1, 2)[0]
            text_x = button1_x + (button_width - text_size[0]) // 2
            text_y = button_y + (button_height + text_size[1]) // 2 
            cv2.putText(frame, 'G', (text_x, text_y), font, 1, text_colors[0], 2, cv2.LINE_AA)

            # Write "R" in the middle of the second rectangle
            text_size = cv2.getTextSize('R', font, 1, 2)[0]
            text_x = button2_x + (button_width - text_size[0]) // 2
            cv2.putText(frame, 'R', (text_x, text_y), font, 1, text_colors[1], 2, cv2.LINE_AA)

            # Write "B" in the middle of the third rectangle
            text_size = cv2.getTextSize('B', font, 1, 2)[0]
            text_x = button3_x + (button_width - text_size[0]) // 2
            cv2.putText(frame, 'B', (text_x, text_y), font, 1, text_colors[2], 2, cv2.LINE_AA)

            
           # Check if the thumb tip, index tip, and midpoint are within any button rectangle
            if is_within_button(thumb_x, thumb_y, index_x, index_y, midpoint_x, midpoint_y, button1) and not button1_pressed and distance_in_cm < 2:
                cv2.putText(frame, '1', (button1[0][0] + 40, button1[0][1] + 60), font, 2, (0, 255, 0), 3)
                ser.write(b'1')  # Sending '1' to Arduino
                print(1)
                button1_pressed = True  # Mark button1 as pressed
            elif not is_within_button(thumb_x, thumb_y, index_x, index_y, midpoint_x, midpoint_y, button1) and button1_pressed:
                button1_pressed = False  # Reset button1 state when fingers leave the area

            if is_within_button(thumb_x, thumb_y, index_x, index_y, midpoint_x, midpoint_y, button2) and not button2_pressed and distance_in_cm < 2:
                cv2.putText(frame, '2', (button2[0][0] + 40, button2[0][1] + 60), font, 2, (0, 0, 255), 3)
                ser.write(b'2')  # Sending '2' to Arduino
                print(2)
                button2_pressed = True  # Mark button2 as pressed
            elif not is_within_button(thumb_x, thumb_y, index_x, index_y, midpoint_x, midpoint_y, button2) and button2_pressed :
                button2_pressed = False  # Reset button2 state when fingers leave the area

            # Check if the thumb tip, index tip, and midpoint are within button3 rectangle
            if is_within_button(thumb_x, thumb_y, index_x, index_y, midpoint_x, midpoint_y, button3) and not button3_pressed and distance_in_cm < 2:
                cv2.putText(frame, '3', (button3[0][0] + 40, button3[0][1] + 60), font, 2, (255, 0, 0), 3)
                ser.write(b'3')  # Sending '3' to Arduino
                print(3)
                button3_pressed = True  # Set the flag to True once the button is pressed

            # Reset the flag if fingers are outside the button3 rectangle
            elif not is_within_button(thumb_x, thumb_y, index_x, index_y, midpoint_x, midpoint_y, button3) and button3_pressed :
                button3_pressed = False  # Reset the flag when fingers leave the button area
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
