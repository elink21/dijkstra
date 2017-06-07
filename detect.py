import cv2
import numpy as np
img2=cv2.imread("last.png")
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,80,120,apertureSize = 5)
minLineLength = 70
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/270,100,minLineLength,maxLineGap)
for line in lines:
	for x1,y1,x2,y2 in line:
		cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)
		cv2.line(img2,(x1,y1),(x1+10,y1+10),(255,0,0),5)
		cv2.line(img2,(x2,y2),(x2+1,y2+1),(0,0,255),5)
cv2.imshow("X1,Y1", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()