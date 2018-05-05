import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
import cv2

#read in an image
image = mpimg.imread('test_images/solidWhiteRight.jpg')

#print out some stats and plots
print('This image is:', type(image), 'with dimensions:', image.shape)
plt.imshow(image)

#cv2.inRange() for color selection
#cv2.fillPoly() for regions selection
#cv2.line() to draw lines on an image given endplots
#cv2.addWeighted() to add/overlay two images cv2.cvtColor() to grayscale or change color
#cv2.bitwise_and() to apply a mask to an image

import math
def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold):
	return cv2.Canny(img, low_threshold， high_threshold)

def gaussian_blur(img, kernel_size)
	return cv2.GaussianBlur(img, (kernel_size, kernel_size),0)

def region_of_interest(img, vertices):
	#define a blank mask to start with
	mask = np.zeros_like(img)

	#define a 3 channel or 1 channel color to filll the mask
	if len(img.shape) > 2
		channel_count = img.shape[2]
		ignore_mask_color = (255,) * channel_count
	else:
		ignore_mask_color= 255

	#fill pixels inside the polygon defined by "vertices" with the fill color
	cv2.fillPoly(mask, vertices, ignore_mask_color)

	#return the image onlu where mask pixels are nonzero
	masked_image = cv2.bitwise_and(img, mask)
	return masked_image

def draw_lines(img, lines, color[255, 0, 0], thickness=2)
	return something