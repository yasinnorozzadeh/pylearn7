import cv2
image = cv2.imread("picture/3.jpg")
print(image.shape)
rimage = cv2.rotate(image, cv2.ROTATE_180)
rimage = cv2.resize(rimage, (600, 500))
cv2.imshow("output", rimage)
cv2.waitKey()