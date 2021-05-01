import cv2
import numpy as np 

app = cv2.imread('apple.jpg')
ora = cv2.imread('orange.jpg')

#a_o = np.hstack((app[:,:256],ora[:,256:]))

cv2.imshow('APPLE_ORANGE',a_o)
cv2.imshow('APPLE',app)
cv2.imshow('ORANGE',ora)

cv2.waitKey(0)
cv2.destroyAllWindows()
