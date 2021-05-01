import cv2
import numpy as np
#im = cv2.imread("lena.jpg",1)
im = np.zeros([480,640,3],np.uint8)		#through numpy.....

im = cv2.line(im,(0,0),(250,300),(255,0,0),5)		#4th arg is BGR Format and 5th is thickness
im = cv2.arrowedLine(im,(20,20),(300,350),(147,96,44),10)
im = cv2.rectangle(im,(10,200),(300,350),(0,255,255),-1)		#-1 so it's fill color that we provide
im = cv2.circle(im,(153,275),75,(0,255,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
im = cv2.putText(im,'Umang',(50,100),font,4,(100,255,255),7,cv2.LINE_AA)		#4 is a font size........
cv2.imshow("Picture",im)


cv2.waitKey(0)
cv2.destroyAllWindows()
