import cv2

# cv2.imwrite('/Users/kentoueta/Desktop/blueImage.jpg', img)
img = cv2.imread('blueImage.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
