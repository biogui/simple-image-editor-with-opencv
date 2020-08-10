import cv2
import numpy as np

def sharpen(image):
	kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
	newImage = cv2.filter2D(image, -1, kernel)

	return newImage

img = cv2.imread("bird2.jpg")
cv2.imwrite("sharpenBird.jpg", img)