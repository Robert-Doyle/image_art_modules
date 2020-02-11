"""
Gif-Maker in Python3
Author: Robert Doyle

Work in Progress

A collection of methods pertaining to the creation of GIFs
and operations regarding them.
"""

import imageio
import natsort
import os, sys

IMAGE_EXTENSIONS = ('.gif','.png','.jpg')


"""
Input:  imageSequence - A folder containing the images to be used.
		newfilename - The filename of the gif to be created.
		timePerFrame - The duration of each frame
Output: None
Creates a gif from the seuqence of input images.
Assembles the gif in alphabetical order of image names.
Note: Filenames are ordered lexicographically at this point in time
"""
def makeSequentialGif(imageFolderPath, newfilename, timePerFrame):
	imFolder = os.listdir(imageFolderPath)
	validImages = [imageio.imread(imageFolderPath +'/'+ x)\
		for x in natsort.natsorted(imFolder) if x.endswith(IMAGE_EXTENSIONS)]

	imageio.mimsave(newfilename + '.gif', validImages, duration=(float(timePerFrame)))
	return



"""
Input: filename - a filename of an image
Output: None
Creates a series of images based on the frames of the gif.
The individual frame images are also in the gif format
May be changed to include png or jpg output in the future
"""
def gifToImages(filename):
	gif = imageio.get_reader(filename)
	gifTitle = filename.split(".gif")
	i = 0
	for frame in gif:
		imageio.imwrite(gifTitle[0] + str(i) + ".gif", frame)
		i += 1
	return