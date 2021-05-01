import cv2
import datetime
cap = cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,1080)		#3  for width
cap.set(4,720)		#4 for height

print(cap.get(3))
print(cap.get(4))
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#save = cv2.VideoWriter("save.avi",fourcc,20.0,(640,480))	#20.0 is a frames per seconds & 640*480 size
while (cap.isOpened()):
		tf,frame = cap.read()

		if tf == True:
			#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #convert our cam into gray........
			font = cv2.FONT_HERSHEY_SIMPLEX
			text = "WIDTH = " + str(cap.get(3)) + " HEIGHT = " + str(cap.get(4))
			frame=cv2.putText(frame,text,(20,100),font,2,(255,0,0),2,cv2.LINE_AA)
			dt = str(datetime.datetime.now())
			frame=cv2.putText(frame,dt,(10,50),font,1,(255,255,0),2,cv2.LINE_AA)
			cv2.imshow("Our video",frame)
#			save.write(frame)				#y not save in gray mode.........?

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
		 	break		
cap.release()
#save.release()
cv2.destroyAllWindows()

	


