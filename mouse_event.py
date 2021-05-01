import numpy as np 
import cv2

# eve = [i for i in dir(cv2) if 'EVENT' in i]
# print(eve)



def click(eve,x,y,flags,param):
	if eve == cv2.EVENT_LBUTTONDOWN:
		
		# cv2.circle(img,(x,y),5,(0,255,255),-1)
		# points.append((x,y))
		# if len(points)>= 2:
		# 	cv2.line(img,points[-1],points[-2],(255,255,0),3)		#last and seclast point is connect............
		# cv2.imshow("IMAGE",img)

			b = img[x,y,0]
			g = img[x,y,1]
			r = img[x,y,2]

			#cv2.circle(img,(x,y),3,(0,255,255),-1)
			mycolorimg = np.zeros((512,512,3),np.uint8)
			mycolorimg[:] = [b,g,r]
			cv2.imshow("NEW IMAGE",mycolorimg)

























		# print(x, "  ",y)
		# font = cv2.FONT_HERSHEY_SIMPLEX
		# strtext = str(x) + "  " + str(y)
		# cv2.putText(img,strtext,(x,y),font,1,(255,255,0),3)	#here don't write img on left side
		# cv2.imshow("IMAGE",img)
	# if eve == cv2.EVENT_RBUTTONDOWN:
	# 	b = img[x,y,0]
	# 	g = img[x,y,1]
	# 	r = img[x,y,2]
	# 	font = cv2.FONT_HERSHEY_SIMPLEX
	# 	strtext = str(b) + "  " + str(g) + "  " + str(r)
	# 	cv2.putText(img,strtext,(x,y),font,.5,(0,250,150),2)	#here don't write img on left side
	# 	cv2.imshow("IMAGE",img)
#img = np.zeros([512,512,3],np.uint8)
img = cv2.imread("lena.jpg",1)
cv2.imshow("IMAGE",img)
points = []
cv2.setMouseCallback("IMAGE",click)

cv2.waitKey(0)

cv2.destroyAllWindows()
