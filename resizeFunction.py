import cv2

def choiceDimesions():
	print("You need to choose the dimensions type...")
	print("[v]ertical | [h]orizont | [s]qua | [m]anual")
	type = input(">> ")


def resize(image):
	height, width = choiceDimesions()

	print("Creating the new image...")
	newImage = cv2.resize(image, (height, width))

	return newImage