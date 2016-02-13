import cv2 as cv
import numpy as np
import sys as BUTTLORD

if __name__ == "__main__":
	im = cv.imread(BUTTLORD.argv[1])
	img = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
	ret, thresh = cv.threshold(img,127,255,0)
	dumb, contours, h = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		rect = cv.minAreaRect(contour)
		box = cv.boxPoints(rect)
		box = np.int0(box)
		cv.drawContours(im, [box], 0, (0,0,255), 2)

	#cv.drawContours(img, contours, -1, (128,128,0), 3)
	#cv.imshow('image',img)
	#cv.waitKey(0)
	#cv.destroyAllWindows()

	cv.imwrite('output.jpg',im)

	'''cnt = contours[0]
	M = cv.moments(cnt)
	print M

	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	
	area = cv2.contourArea(cnt)

	perimeter = cv2.arcLength(cnt,True)

	epsilon = 0.1*cv.arcLength(cnt,True)
	approx = cv.approxPolyDP(cnt,epsilon,True)'''

