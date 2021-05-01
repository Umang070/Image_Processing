import cv2
import numpy as np 

img = np.zeros((250,500,3),np.uint8)
img = cv2.rectangle(img,(100,0),(250,200),(255,255,255),-1)
img1 = cv2.imread("img_1.png")
bitAnd = cv2.bitwise_and(img1,img)

cv2.imshow("IMAGE",img)
cv2.imshow("IMAGE",img1)

cv2.imshow("BITAND",bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()