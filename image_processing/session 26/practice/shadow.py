import cv2
import numpy as np
# img = np.arange(0, 1 , 1, np.uint8)
# img = np.zeros((350, 700), dtype = np.uint8)
img = np.ones((250, 500), dtype = np.uint8,)

h, w = img.shape
for i in range (h):
    for j in range(w):
        img[i,j]= (i*-1) - 255 
cv2.imshow("output (#_#)" , img)
cv2.waitKey()