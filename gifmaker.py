"""
Gif-Maker in Python3
Author: Robert Doyle

Work in Progress

A collection of methods pertaining to the creation of GIFs
and operations regarding them.
"""

import imageio
import os, sys


"""
Input:  imageSequence - An array of image filenames to make a gif from
		filename - The filename of the gif to be created.
Output: None
Creates a gif from the seuqence of input images.
"""
def makeSequentialGif(frameLength, imageSequence):

	
	return



"""
Input: filename - a filename of an image
Output: None
Creates a series of images based on the frames of the gif.
"""
def gifToImages(filename):
	gif = imageio.get_reader(filename)
	gifTitle = filename.split(".gif")
	i = 0
	for frame in gif:
		imageio.write(gifTitle + str(i) + ".gif", frame)
		i++

	return

# 