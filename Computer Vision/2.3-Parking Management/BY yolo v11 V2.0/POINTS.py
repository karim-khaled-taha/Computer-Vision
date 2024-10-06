import cv2
import numpy as np

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

# Load the video file (replace 'your_video.mp4' with your video file path)
video_path = 'carPark.mp4'  # Change this to the path of your video file
cap = cv2.VideoCapture(video_path)

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', POINTS)

area1=[(242, 90),(43, 95),(37, 666),(261, 662)]
area2=[(394, 82),(409, 664),(616, 667),(620, 92)]
area3=[(748, 81),(857, 83),(870, 655),(747, 671)]
area4=[(897, 139),(1010, 138),(995, 652),(910, 652)]

while cap.isOpened():
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    if not ret:
        print("End of video")
        break

    
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,255,0),2)
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(0,255,0),2)
    cv2.polylines(frame,[np.array(area3,np.int32)],True,(0,255,0),2)
    cv2.polylines(frame,[np.array(area4,np.int32)],True,(0,255,0),2)

    cv2.imshow('FRAME', frame)


    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
