import numpy as np
import cv2

imgC = np.zeros((400, 400, 3), np.uint8)
cv2.circle(imgC, (200, 200), 50, (255, 0, 0), 1)
cv2.imwrite('circle1.jpg', imgC)
cv2.imshow('img1', imgC)

imgC = np.zeros((400, 400, 3), np.uint8)
cv2.circle(imgC, (200, 200), 100, (0, 255, 0), 3)
cv2.imwrite('circle2.jpg', imgC)
cv2.imshow('img2', imgC)

imgC = np.zeros((400, 400, 3), np.uint8)
cv2.circle(imgC, (200, 200), 150, (0, 0, 255), -1)
cv2.imwrite('circle3.jpg', imgC)
cv2.imshow('img3', imgC)

cv2.waitKey(0)
cv2.destroyAllWindows()
