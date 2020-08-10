import cv2

def blur(image, nv):
	# kernels = [1, 3, 5, 9, 11]
	# k = kernels[nv]
	# newImage = cv2.blur(image, (k, k))

	kernel = 5
	newImage = cv2.blur(image, (kernel, kernel))

	return newImage