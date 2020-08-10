import cv2

def resize(image, height, width):
	originalH, originalW = image.shape[0:2]

	if originalW <= originalH:
		newImage = cv2.resize(image, (height, width))
	else:
		newImage = cv2.resize(image, (width, height))

	return newImage