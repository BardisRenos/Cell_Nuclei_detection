#! /usr/bin python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from skimage import color
from util import *


def convert_to_gray_scale(image):
    image_to_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_to_gray


def image_preprocessing(given_image):
    image_gray_scale = convert_to_gray_scale(given_image)
    _, image_threshold_bw = cv2.threshold(image_gray_scale, 100, 255, cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    image_morph = cv2.morphologyEx(image_threshold_bw, cv2.MORPH_CLOSE, kernel, iterations=3)
    image_mask = 255 - image_morph

    background = cv2.dilate(image_mask, kernel, iterations=2)
    show_2_images_with_matplot(image_threshold_bw, image_mask, "BW", "morph")
    dist_transform = cv2.distanceTransform(image_mask, cv2.DIST_L2, 3)
    _, foreground = cv2.threshold(dist_transform, 0.285 * dist_transform.max(), 255, 0)
    the_unknown_image = background - foreground
    foreground = np.uint8(foreground)

    # return foreground, the_unknown_image

    # def markers_creation():
    #     # foreground, the_unknown_image = image_preprocessing(given_image)
    #     _, image_markers = cv2.connectedComponents(foreground, connectivity=8)
    #     image_markers = image_markers + 10
    #     image_markers[the_unknown_image == 255] = 0
    #
    #     # return image_markers
    #
    # def watershed():
    #     # image_markers = markers_creation()
    #     image_markers = cv2.watershed(pure_image, image_markers)
    #     pure_image[image_markers == -1] = [0, 255, 0]
    #     image_label2rgb = color.label2rgb(image_markers, bg_label=0)

    # return image_label2rgb


if __name__ == '__main__':
    image_path = '/home/renos/Pictures/sample_3.png'
    image = read_image(image_path)

    # show_image_with_matplot(image[:, :, 0])
    image_preprocessing(image)
