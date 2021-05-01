import cv2

img = cv2.imread("messi5.jpg")
img1 = cv2.imread("lena.jpg")

print(img.size)			#row,col and channel........
print(img.shape)		#returns total num of pixels.......
print(img1.shape)
# b,g,r = cv2.split(img)
# print(b)
# img = cv2.merge((b,g,r))

ball  = img[280:340,330:390]		#region of interest.......
img[273:333,100:160] = ball
img = cv2.resize(img,(512,512))		#resize the image........
img1 = cv2.resize(img1,(512,512))
#mimage = cv2.add(img,img1)
mimage = cv2.addWeighted(img,.7,img1,.3,0)
cv2.imshow("IMAGE",mimage)
#cv2.imshow("IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
