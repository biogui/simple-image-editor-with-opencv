from cv2 import filter2D
import numpy as np

def sharpen(image):
	kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

	print("Creating the new image...")
	newImage = filter2D(image, -1, kernel)

	return newImage