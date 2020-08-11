from cv2 import blur as bCV

def blur(image):
	print("Choice the blur intensity")
	print("0 - very weak")
	print("1 - weak")
	print("2 - avarage")
	print("3 - strong")
	print("4 - very strong")
	i = int(input(">> "))

	kernels = [1, 3, 5, 9, 11]
	k = kernels[i]

	print("Creating the new image...")
	newImage = bCV(image, (k, k))

	return newImage