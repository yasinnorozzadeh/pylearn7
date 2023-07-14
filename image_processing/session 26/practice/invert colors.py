import cv2
img = cv2.imread("picture/2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = img.shape
for i in range(height):
    for j in range(width):
        img[i, j] = 255 - img[i, j]

cv2.imshow("output", img)
cv2.waitKey()
cv2.imwrite("test2.jpg", img)