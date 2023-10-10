import cv2
import numpy as np

img=cv2.imread("images/cards.jpg")
width,height=250,350
pts1=np.float32([[247,57],[319,79],[215,157],[287,182]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix= cv2.getPerspectiveTransform(pts1,pts2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("1",img)
cv2.imshow("",imgoutput)

cv2.waitKey(0)