# Two kinds of HOUGHLINE TRANSFORMATION-------
# 1)_-------The Standard Hough Transform (HoughLines method)
# 2)--------The Probabilistic 
import numpy as np 
import cv2

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,30,120,apertureSize=3)
cv2.imshow('EDGED',edges)
#lines = cv2.HoughLines(edges,1,np.pi/180,200)	#1 is value of r...distance resolution of the accumulator in pixels 
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)	#100 is thrsold means after 100 value line is consider
for line in lines:
	x1,y1,x2,y2 = line[0]
	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# for line in lines:
# 	r,theta = line[0]
# 	a = np.cos(theta)
# 	b = np.sin(theta)
# 	x = r*a
# 	y = r*b
# 	#x1 = (r*cos(theta) - 1000*sin(theta))
# 	x1 = int(x + 1000*(-b))
# 	y1 = int(y + 1000*(a))
# 	#x2 = (r*cos(theta) + 1000*sin(theta))
# 	x2 = int(x - 1000*(-b))
# 	y2 = int(y - 1000*(a))

# 	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('IMAGE',img)
q = cv2.waitKey(0)
cv2.destroyAllWindows()