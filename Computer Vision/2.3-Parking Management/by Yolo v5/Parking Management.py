import cv2
import torch
import numpy as np


def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', POINTS)            
    
           


model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #use any fourcc type to improve quality for the saved video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) #Video settings

cap=cv2.VideoCapture('parking.mp4')



area = [(26,433),(9,516),(389, 492),(786,419),(720,368)]
area2 =[(985,345),(856,384),(814,348),(946,317)]
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.resize(frame,(1020,600))

    results=model(frame)
    #print(results.xyxy[0])
    #print(results.pandas().xyxy[0])
    #results.pandas()
    points = []
    for index, row in results.pandas().xyxy[0].iterrows():
        #print(row)
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        d=(row['name'])
        cx=int(x1+x2)//2
        cy=int(y1+y2)//2
        

        if 'car' in d:
            results = cv2.pointPolygonTest(np.array(area,np.int32),(cx,cy),False)
            results2 = cv2.pointPolygonTest(np.array(area2,np.int32),(cx,cy),False)
            #print(results)
            if results>=0 or results2>=0:
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
                cv2.putText(frame,str(d),(x1,y1),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
                points.append([cx])
    a = len(points)
    #print(points)
    cv2.polylines(frame,[np.array(area,np.int32)],True,(0,255,0),2)
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(0,255,0),2)
    cv2.putText(frame,'number of cars in parking ='+str(a),(50,80),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                
    cv2.imshow("FRAME",frame)
    out.write(frame) #save your video
    #cv2.setMouseCallback("FRAME",POINTS)
   

    if cv2.waitKey(10)==27:
        break
cap.release()
out.release()

cv2.destroyAllWindows()