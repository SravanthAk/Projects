import cv2
import numpy as np

def empty(a):
    pass
framewidth=300
frameheight=300
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",26,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)




while True:
    success, img = cap.read()

    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
    sat_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    sat_max=cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min=cv2.getTrackbarPos("Val Min","TrackBars")
    v_max=cv2.getTrackbarPos("Val Max","TrackBars")
    #print(h_min,h_max,sat_min,sat_max,v_min,v_max)
    lower=np.array([h_min,sat_min,v_min])
    upper=np.array([h_max,sat_max,v_max])
    mask=cv2.inRange(imghsv,lower,upper)
    res=cv2.bitwise_and(img,img,mask=mask)
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([img,mask,res])
    cv2.imshow("Result", hstack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break