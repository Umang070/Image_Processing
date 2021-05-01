import numpy as np 
import cv2

cap = cv2.VideoCapture('vtest.avi')

flag,frame1 = cap.read()
flag,frame2 = cap.read()
while cap.isOpened():
	
	dif = cv2.absdiff(frame1,frame2)
	gray = cv2.cvtColor(dif,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	_,th = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
	dilated = cv2.dilate(th,None,iterations=3)		#kernel ize = NULL
	contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for c in contours:
		(x,y,w,h) = cv2.boundingRect(c)

		if cv2.contourArea(c) < 900:
			continue
		cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,255),3)
		cv2.putText(frame1,"STATUS : {}".format("MOVEMENT"),(10,30),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),3)
		cv2.imshow("VIDEO_",frame1)

	frame1 = frame2
	flag,frame2 = cap.read()



	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()