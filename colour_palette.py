#Determines a colour palette from an image
#Author: Robert-Doyle 2020
#Requirements Pillow

from PIL import Image
import sys



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

print(colour_palette(sys.argv[1], sys.argv[2]))
sys.exit()