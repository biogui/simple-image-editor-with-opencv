import cv2
import numpy as np

def sharpen(image, nv):
	kernel = np.ones((5, 5), np.float32)/25

	print("Creating the new image...")
	newImage = cv2.filter2D(image, -1, kernel)

	return newImage