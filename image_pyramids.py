#PYRAMID------Is a type of multiscale signal representation in which a image is subject to repeated smoothing &  subsampling...

import cv2
import numpy as np 

img = cv2.imread('lena.jpg')

# lr = cv2.pyrDown(img)
# hr = cv2.pyrUp(lr)
# cv2.imshow('IMAGE-HIGHER_RESOLUTION',hr)

layer = img.copy()
gp = [layer]

for i in range(6):
	layer = cv2.pyrDown(layer)
	gp.append(layer)  
#	cv2.imshow(str(i),layer)

layer = gp[5]		#lastt image
cv2.imshow("Lower_Level_Gaussian",layer)
lp = [layer]

for i in range(5,0,-1):
	Gaussian_Extended = cv2.pyrUp(gp[i])
	Laplacian = cv2.subtract(gp[i-1],Gaussian_Extended)
	cv2.imshow(str(i),Laplacian)

cv2.imshow('IMAGE',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
