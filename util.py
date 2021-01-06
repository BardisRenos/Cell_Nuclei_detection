#! /usr/bin python3
# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt
from skimage.segmentation import clear_border


# Reading an image and returning the image
def read_image(path):
    return cv2.imread(path)


# Remove cells that are touching the edge of the image
def clear_borders(image):
    return clear_border(image)


# Showing two images by using Matplotlib library
def show_2_images_with_matplot(image1, image2, title1, title2):
    plt.figure(figsize=(20, 12))
    plt.subplot(121), plt.imshow(image1, cmap='gray'), plt.title(title1)
    plt.subplot(122), plt.imshow(image2, cmap='gray'), plt.title(title2)
    plt.show()


# Showing the image by using OpenCV
def show_image_with_matplot(image1):
    plt.imshow(image1, cmap='gray'), plt.title("Given Image")
    plt.show()
