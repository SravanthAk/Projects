import cv2
import numpy as np

def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        #print(area)
        if area>100:
            cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0),2 )
            peri=cv2.arcLength(cnt,True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objcor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
            if objcor==3:
                objtype="Tri"
            elif objcor==4:
                aspratio=w/float(h)
                if aspratio>0.95 and aspratio<1.05:
                   objtype="Square"
                else:
                   objtype="Rectangle"
            elif objcor==6:
                objtype="Hexagon"
            elif objcor>6:
                objtype="Circle"
            else:
                objtype="Right angle triangle"
            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(imgcontour,objtype,(x+(w//2)-30,y+(h//2)),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),1)



img=cv2.imread("images/shapes.png")
imgcontour=img.copy()
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),1)
imgcanny=cv2.Canny(imgblur,50,50)
getcontours(imgcanny)


cv2.imshow("img",img)
#cv2.imshow("gray",imggray)
#cv2.imshow("blur",imgblur)
#cv2.imshow("canny",imgcanny)
cv2.imshow("contour",imgcontour)




cv2.waitKey(0)