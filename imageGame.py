import cv2
from PIL import Image
import io
import base64
import numpy as np


def getErrorScore(data_1, data_2):

    binary_data_1= base64.b64decode(data_1)
    image_buffer_1 = io.BytesIO(binary_data_1)
    p_img1 = Image.open(image_buffer_1)
    arr_1 = np.array(p_img1)
    img1 = cv2.cvtColor(arr_1, cv2.COLOR_RGB2BGR) 

    binary_data_2= base64.b64decode(data_2)
    image_buffer_2 = io.BytesIO(binary_data_2)
    p_img2 = Image.open(image_buffer_2)
    arr_2 = np.array(p_img2)
    img2 = cv2.cvtColor(arr_1, cv2.COLOR_RGB2BGR) 



    ksize = (70,70)
    img1 = cv2.blur(img1, ksize)
    img2 = cv2.blur(img2, ksize)

    h, w, c= img1.shape
    diff = cv2.subtract(img2, img1)
    err = np.sum(diff**2)
    mse = err/(float(h*w))

    return mse
