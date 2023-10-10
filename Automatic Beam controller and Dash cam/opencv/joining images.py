import cv2
import numpy as np
img=cv2.imread("images/PHOTO.jpeg")
hor=np.hstack((img,img))
ver=np.vstack((img,img))

cv2.imshow("hor",hor)
cv2.imshow("",ver)

cv2.waitKey(0)
