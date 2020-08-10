import cv2

def blur(image):
	kernel = 5
	newImage = cv2.blur(image, (kernel, kernel))

	return newImage