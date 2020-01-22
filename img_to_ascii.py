#Converts an image into ascii art
#Author: Robert-Doyle 2019
#Requirements Numpy, Scipy, Pillow, imageio

from PIL import Image
import imageio
import os, sys


"""
Input: An RGB value tuple
Output: A 0-1 value based on the whiteness of the pixel
Converts a coloured pixel to a black and white pixel of equivalent brightness
"""
def toBWVal(pixel):
	return (((pixel[0] + pixel[1] + pixel[2]) / 3) / 255)


"""
Input: An image filename string
Output: None
Creates a greyscale rendition of the input image
"""
def toBW(filename):

	im = imageio.imread(filename)

	for row in im:
		for pix in row:
			adjustedVal = toBWVal(pix) * 255
			pix[0] = adjustedVal
			pix[1] = adjustedVal
			pix[2] = adjustedVal
			
	imageio.imwrite("bw" + filename, im)



"""
Input: A pixel list, the current pixel index, the compression block width and height
and the image width and height
Output: A compressed pixel value
Returns a value representing the average brightness of a block of pixels
"""
def compressPixels(pixels, topLeftIndex, blockWidth, blockHeight, w, h):
	vals = []
	for i in range(0, blockHeight):
		for j in range(0, blockWidth):
			currentPixel = topLeftIndex + (i * w) + j
			if (currentPixel < w * h):
				vals.append(toBWVal(pixels[currentPixel]))

	compressedVal = 0
	for val in vals:
		compressedVal += val
	compressedVal = compressedVal / len(vals)
	return (int)(compressedVal * 126 // 1)



"""
Inputs: A list of rgb pixels, image and output parameters
Outputs a list of characters representing the pixels
Converts a pixel list into an ascii text representation
"""
def convertPixels(pixels, charwidth, charHeight, w, h):
	imgChars = []

	blockWidth = (int)(w / charwidth)
	blockHeight = (int)(h / charHeight)

	index = 0
	row = 0
	column = 0
	while (row < charHeight):
		imgChars.append((chr)((compressPixels(\
			pixels, (index + row * (blockHeight * w)) + column * blockWidth,\
			 blockWidth, blockHeight, w, h))))
		column += 1
		if (column >= charwidth):
			column = 0
			row += 1

	return imgChars


"""
Input : An image filename string
Output: None
Creates a visual ascii text aproximation of an image file
"""
def imgToAscii(filename):
	im = Image.open(filename)
	w, h = im.size

	# A square image gets distorted to a width height ratio of 7:11
	charwidth = w/7
	charHeight = h/11

	imgChars = convertPixels(list(im.getdata()), charwidth, charHeight, w, h)

	outputFilename = im.filename.replace(".jpg", ".txt")
	outputFilename = outputFilename.replace(".png", ".txt")

	outputFile = open(outputFilename, 'w', encoding='ascii', errors='replace')

	count = 0

	for char in imgChars:
		outputFile.write(char)
		count += 1
		if (count >= charwidth):
			outputFile.write('\n')
			count = 0
		
	outputFile.close()
	return

"""
"""
def failureFunction():
	print("Invalid argument")
	print("Please include your argument in the form 'image_filename mode'")
	print("Where mode is either 'bw' or 'text'")
	sys.exit()


if (len(sys.argv) != 3):
	failureFunction()
else:
	currentImage = sys.argv[1]
	if (sys.argv[2] == 'bw'):
		toBW(currentImage)
	elif (sys.argv[2] == 'text'):
		imgToAscii(currentImage)
	else:
		failureFunction()