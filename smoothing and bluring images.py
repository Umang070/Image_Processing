import cv2
from matplotlib import pyplot as plt 
import numpy as np 

img = cv2.imread("lena.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 

kernel = np.ones((5,5),np.float32)/25	#1/height of matrix * width of matrix(5*5)
dst = cv2.filter2D(img,-1,kernel)	#-1 is depth
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)	#0 is sigma......for removing high frequency noise ....
median = cv2.medianBlur(img,5)		#solt & paper dots..
bfilter = cv2.bilateralFilter(img,9,70,70)	#sigma color and sigma space . for edegess sharpeS
titles = ['IMAGE','2D CONVOLUTION','BLUR','GaussianBlur','medianBlur','bilateralFilter']
images = [img,dst,blur,gblur,median,bfilter]

for i in range(6):
	plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()
