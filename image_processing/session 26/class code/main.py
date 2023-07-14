import cv2

image = cv2.imread("stars.jpg")
my_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# print(my_image)
# print(my_image.shape)
print(my_image[550, 800]) # 1
# my_image[550, 800] = 250
my_image[520: 570, 780:840] = 250
cv2.imshow(None, my_image)
cv2.waitKey()
cv2.imwrite("resul.jpg", my_image)