# --------------------------------------------------------------------- #
# File: ImageProcessing_Project.py
# Author: Mahalia Phillips
# Purpose: This code will perform a specific type of image
#          processing. Ideas for Image Processing are smile 
#          detection, and detection of the corner of an image. 
# Version: 10/27/25
#          10/30/25
# Resources: I will attach a link or make a document for all of
#            the resources I used.
# --------------------------------------------------------------------- #

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ----- Original Image ----- #

image_path = '/Users/mahaliaphillips/Documents/CS_315/IMG_9766.jpeg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title('Gabe')
plt.axis('off')
plt.show()

# ----- Resized Image ----- #

resized_image = cv2.resize(image_rgb, (1900, 800))

plt.imshow(resized_image)
plt.title('Gabe Squashed')
plt.axis('off')
plt.show()

# ----- Gaussian Blurred Image ----- #

Gaussian_blurred_image = cv2.GaussianBlur(image_rgb, (125, 125), 0) 
# The "15" values tell the kernel how much the photo should be blurred.
# Note: The kernel size must always be positive and odd.

plt.imshow(Gaussian_blurred_image)
plt.title('Gabe Blurred')
plt.axis('off')
plt.show()

# ----- Greyscaled Image ----- #

grey_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

plt.imshow(grey_image, cmap='gray')
plt.title('Gabe Grey')
plt.axis('off')
plt.show()

# Create Image Edge Detector


# Create Smile Detector
