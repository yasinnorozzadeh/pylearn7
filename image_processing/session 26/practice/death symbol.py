# The first solution

# import cv2
# img = cv2.imread("picture/img.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (600, 600))
# height, width = img.shape
# for i in range(250):
#     if i <= 100:
#         for j in range(100-i, 250-i):
#             if j >= 0:
#                 img[i, j] = 0
#     else:
#         for j in range(0, 250-i):
#             if j >= 0:
#                 img[i, j] = 0
# cv2.imshow("output", img)
# cv2.waitKey()



# The second solution

# import cv2
# img = cv2.imread("picture/img.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (600, 600))
# cv2.line(img,(10,150),(150,10),(0, 0, 0), 100 )
# cv2.imshow("output", img)
# cv2.waitKey()



# The third solution

import cv2
import numpy as np
img = cv2.imread("picture/img.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (600, 600))
pt1 = (100, 0)
pt3 = (0, 250)
pt2 = (0, 100)
pt4 = (250, 0)
triangle_cnt = np.array( [pt1, pt2, pt3, pt4] )
cv2.drawContours(img, [triangle_cnt], 0, (0,0,0), -1)
cv2.imshow("output", img)
cv2.waitKey()
cv2.imwrite("output.jpg", img)