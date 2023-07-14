import cv2
import numpy as np


width=height=400
img = np.ones((width, height), dtype = np.uint8)
img [:,:] = 255
color = (0, 0, 0)
# cv2.line(img, (50, 50), (350, 50), color, 30) 
# pt1 = (100, 0)
# pt3 = (0, 250)
# pt2 = (0, 100)
# pt4 = (250, 0)
# triangle_cnt = np.array( [pt1, pt2, pt3, pt4] )
# cv2.drawContours(img, [triangle_cnt], 0, (0,0,0), -1)
# cv2.line(img, (130, 150), (270, 290), color, 30)
cv2.ellipse(img, (230, 165), (70, 70), -50, 140, 360, (0,0,0), thickness=30)
cv2.ellipse(img, (180, 290), (70, 70), 140, 140, 360, (0,0,0), thickness=30)

cv2.imshow('test', img)
cv2.waitKey()