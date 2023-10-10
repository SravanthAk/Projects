import cv2  #computer vision

framewidth=640 
frameheight=480
count=0
minarea=500
color=(255,0,0)

nplatecascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml') #location of xml file
cap=cv2.VideoCapture(0) #0 for default camera; 1 for external camera
cap.set(3,framewidth) #id no 3 is for setting frame width
cap.set(4,frameheight) #id no 4 is for setting frame height
cap.set(10,100) #id no 10 is for adjusting brightness

while True:
    success,img=cap.read() 

    imggray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    numberplates = nplatecascade.detectMultiScale(imggray, 1.1, 4) #image,scale factor, min neighbours
    
    for (x, y, w, h) in numberplates:
        area=w*h
        if area>minarea:
            count+=1
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0),1)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)#1-font scale; 2-font thickness
            print("Vehicle detected "+str(count)+" times")
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    