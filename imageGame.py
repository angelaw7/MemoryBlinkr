import cv2
import numpy as np


def getErrorScore(img1, img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    h, w = img1.shape
    diff = cv2.subtract(img2, img1)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse