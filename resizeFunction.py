import cv2

def resize(image, height, width):
	newImage = cv2.resize(image, (height, width))

	return newImage