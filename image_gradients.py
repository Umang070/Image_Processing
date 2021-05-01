#image gradient--------directional change in the intensity or color in an image........
#canny edge detector------detect wide range of edges in images......
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread("messi5.jpg",0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)		#sec is datatype
lap = np.uint8(np.absolute(lap))		#convert to unsigned int


sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)		#dx = 1 and dy = 0
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelxy = cv2.bitwise_or(sobelx,sobely)

canny = cv2.Canny(img,100,200)		#thresold 1 and threaold 2 it is good for edges b'caz no noise

titles = ['IMAGE','Laplacian','sobelx','sobely','sobelxy','Canny']
images = [img,lap,sobelx,sobely,sobelxy,canny]



for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()