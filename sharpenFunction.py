from cv2 import filter2D
import numpy as np

def sharpen(image):
	kernel = np.ones((5, 5), np.float32)/25

	print("Creating the new image...")
	newImage = filter2D(image, -1, kernel)

	return newImage