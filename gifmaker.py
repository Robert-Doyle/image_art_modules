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
def makeSequentialGif(imageSequence, frameLength):
	return