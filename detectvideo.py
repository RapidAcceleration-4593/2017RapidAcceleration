import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

while(True):
	ret, frame = cap.read()
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	
	ret, thresh = cv.threshold(gray, 227, 255, cv.THRESH_BINARY)
	garbage, contours, h = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		rect = cv.minAreaRect(contour)
		box = cv.boxPoints(rect)
		box = np.int0(box)
		cv.drawContours(frame, [box], 0, (0,0,255), 2)


	#cv.drawContours(frame, contours, -1, (0,0,255), 2)
	cv.imshow('frame',frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()
