import cv2
import numpy as np

def sharpen(image, nv):
	# kernels = []

	# k = kernels[nv]
	# newImage = cv2.filter2D(image, -1, k)

	kernel = np.ones((5, 5), np.float32)/25
	newImage = cv2.filter2D(image, -1, kernel)

	return newImage