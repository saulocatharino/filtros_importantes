import cv2
import numpy as np


color = ('b','g','r')
cap = cv2.VideoCapture('vinhetas.mp4')
ratio = .50



lsd = cv2.createLineSegmentDetector(0)
lsd2 = cv2.createLineSegmentDetector(1)
lsd3 = cv2.createLineSegmentDetector(2)
prev = cap.read()[1]

stripz = np.zeros_like(prev)
stripz = np.invert(stripz)
stripz = cv2.resize(stripz, (int(stripz.shape[1]/11),int(stripz.shape[0]/11)))
old_strip = stripz.copy()
for i in range(0,19):
    old_strip = cv2.hconcat([old_strip,stripz])

while True:


	img = cap.read()[1]
	img = cv2.resize(img,(0,0), None,ratio, ratio)


	black = np.zeros_like(img)
	black = np.invert(black)
	img2 = black.copy()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	lines = lsd.detect(gray)[0]
	lines2 = lsd2.detect(gray)[0] 
	lines3 = lsd3.detect(gray)[0]
	for dline in lines:
		    x0, y0, x1, y1 = dline.flatten()

		    cv2.line(black, (x0, y0), (x1,y1), (0,0,0), 1, cv2.LINE_AA)
		    cv2.line(img2, (x0, y0), (x1,y1), (0,255,255), 1, cv2.LINE_AA)

	for dline in lines2:
		    x0, y0, x1, y1 = dline.flatten()

		    cv2.line(black, (x0, y0), (x1,y1), (50,50,50), 1, cv2.LINE_AA)
		    cv2.line(img2, (x0, y0), (x1,y1), (255,0,255), 1, cv2.LINE_AA)

	for dline in lines3:
		    x0, y0, x1, y1 = dline.flatten()

		    cv2.line(black, (x0, y0), (x1,y1), (100,100,100), 1, cv2.LINE_AA)
		    cv2.line(img2, (x0, y0), (x1,y1), (255,255,0), 1, cv2.LINE_AA)

	old_strip = cv2.hconcat([old_strip, cv2.resize(img,(int(old_strip.shape[1]/10),int(old_strip.shape[0])))])
	old_strip = old_strip[0:old_strip.shape[1]*20,old_strip.shape[0]:old_strip.shape[0]*21]
	old_strip = cv2.resize(old_strip, (black.shape[1]*2,old_strip.shape[0]))
	gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
	final1 = cv2.hconcat([img,gray])
	final1 = cv2.vconcat([final1,old_strip]) 

	final2 = cv2.hconcat([black, cv2.cvtColor(img, cv2.COLOR_BGR2HSV)])
	final3 = cv2.vconcat([final1,final2])

	cv2.imshow('Resultado', final3) 
	k = cv2.waitKey(1)
	if k == ord('q'):
		exit()

