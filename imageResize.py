import cv2

def resize(fileName, height, width):
	image = cv2.imread(fileName)
	originalH, originalW = image.shape[0:2]

	if originalW <= originalH:
		newImage = cv2.resize(image, (height, width))
	else:
		newImage = cv2.resize(image, (width, height))

	return fileName, newImage

fileName, newImage = resize("bird.jpg", 960, 1280)

fileName = "new_{}".format(fileName)
cv2.imwrite(fileName, newImage)