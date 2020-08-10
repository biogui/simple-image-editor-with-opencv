import cv2

def blur(image):
	kernel = 5
	newImage = cv2.blur(image, (kernel, kernel))

	return newImage

img = cv2.imread("bird.jpg")

cv2.imwrite("newImg.jpg", blur(img))