import cv2

img = cv2.imread('blueImage.jpg', 0)
cv2.imwrite('ReadWrite.jpg',img)
