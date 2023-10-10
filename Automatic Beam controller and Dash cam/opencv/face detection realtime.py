import cv2

framewidth=640
frameheight=480
facecascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
minarea=500
color=(255,0,0)

cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,200)

while True:
    success,img=cap.read()

    imggray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    face = facecascade.detectMultiScale(imggray, 1.1, 4)

    for (x, y, w, h) in face:
        area=w*h
        if area>minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
            cv2.putText(img,"Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break