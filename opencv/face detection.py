import cv2
import numpy as np

facecascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread("images/4.jpeg")
imggray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces=facecascade.detectMultiScale(imggray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

cv2.imshow("",img)

cv2.waitKey(0)