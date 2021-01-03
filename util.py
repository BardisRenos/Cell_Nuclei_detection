#! /usr/bin python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


def read_image(path):
    return cv2.imread(path)


def show_2_images_with_matplot(image1, image2, title1, title2):
    plt.figure(figsize=(20, 12))
    plt.subplot(121), plt.imshow(image1, cmap='gray'), plt.title(title1)
    plt.subplot(122), plt.imshow(image2, cmap='gray'), plt.title(title2)
    plt.show()


def show_image_with_matplot(image1, title1):
    plt.plot(121), plt.imshow(image1, cmap='gray'), plt.title(title1)
    plt.show()
