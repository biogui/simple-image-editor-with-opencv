from cv2 import resize as rszCV

def choiceDimesions():
	print("You need to choose the resolutions type:")
	print("[v]ertical | [h]orizont | [s]quare | [m]anual")
	type = input(">> ").lower()

	isValidType = False
	while not isValidType:
		if type[0] == "s":
			height, width = 1024, 1024

			isValidType = True
		elif type[0] == "m":
			height = int(input("Enter the height: "))
			width = int(input("now, the width: "))

			isValidType = True
		elif type[0] == "v" or type[0] == "h":
			stdResolutions = [[1024, 728], [1280, 720], [2560, 1080]]

			print("There are three options:")
			print("0 - 4:3 (1024 x 728)")
			print("1 - 16:9 (1280 x 720)")
			print("2 - 21:9 (2560 x 1080)")
			c = int(input("Choose>> "))

			x, y = stdResolutions[c] if type[0] == "h" else stdResolutions[c][::-1]
			height, width = x, y

			isValidType = True
		else:
			type = input("Invalid type. Try again: ")

	return height, width

def resize(image):
	height, width = choiceDimesions()

	print("Creating the new image...")
	newImage = rszCV(image, (height, width))

	return newImage