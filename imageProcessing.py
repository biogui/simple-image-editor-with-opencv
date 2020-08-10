import sys
import os
from fnmatch import fnmatch
from cv2 import imread, imwrite

from imageResize import resize
from imageBlur import blur
from imageSharpen import sharpen

# fileName, newImage = resize("bird.jpg", 960, 1280)

# imwrite("resize_{}".format(fileName), newImage)
# imwrite("blur_{}".format(fileName), blur(newImage))
# imwrite("sharpen_{}".format(fileName), sharpen(newImage))

nArgs = len(sys.argv)
if nArgs == 3:
	height = int(sys.argv[1])
	width = int(sys.argv[2])
else: 
	height = 960
	width = 1280

if not os.path.exists("newImgs"):
	os.makedirs("newImgs")


pathDir = "Imgs"
pattern = "*.jpg"
listOfFiles = os.listdir(pathDir)
for fileName in listOfFiles:
	imagePath = "{}/{}".format(pathDir, fileName)
	image = imread(imagePath)

	if fnmatch(fileName, pattern):
		newImage = resize(image, height, width)
		newImage = blur(newImage)
		newImage = sharpen(newImage)

		newImgPath = "newImgs/{}".format(fileName)
		imwrite(newImgPath, newImage)