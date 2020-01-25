#A collection of methods dealing with images and colours
#Author: Robert-Doyle 2020
#Requirements Pillow

from PIL import Image
import sys


MAX_RGB = 255


"""
Input: A filename string
Output: A list of rgb values of the top-5 most common colours in the image
"""
def colour_palette(filename, n):
	im = Image.open(filename)
	pixels = list(im.getdata())
	colours = {}

	for pix in pixels:
		if (pix in colours):
			colours[pix] += 1
		else:
			colours[pix] = 1

	return sorted(colours, key=colours.get, reverse=True)[:int(n)]



"""
Input: A representation of a colour
Output: an rgb tuple representation of the complimentary colour
to the input colour
"""
def complimentary_colour(colour):
	red = MAX_RGB - colour[0]
	green = MAX_RGB - colour[1]
	blue = MAX_RGB - colour[2]
	return (red, green, blue)


#print(colour_palette(sys.argv[1], sys.argv[2]))
sys.exit()
