import cv2
import numpy as np


def convert_to_gray_scale(self, image):
    image_to_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_to_gray


def image_preprocessing(self, given_image):
    self.convert_to_gray_scale(given_image)
    self.pure_image = given_image

    _, self.image_threshold_bw = cv2.threshold(self.image_gray_scale, 240, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    self.image_morph = cv2.morphologyEx(self.image_threshold_bw, cv2.MORPH_CLOSE, kernel, iterations=9)
    self.image_mask = 255 - self.image_morph

    self.background = cv2.dilate(self.image_mask, kernel, iterations=5)
    self.dist_transform = cv2.distanceTransform(self.image_mask, cv2.DIST_L2, 3)
    _, self.foreground = cv2.threshold(self.dist_transform, 0.285 * self.dist_transform.max(), 255, 0)
    self.the_unknown_image = self.background - self.foreground
    self.foreground = np.uint8(self.foreground)
