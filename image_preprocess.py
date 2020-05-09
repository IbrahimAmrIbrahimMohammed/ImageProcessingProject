#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

#=============================#
def preprocessing_image_to_black_and_white(im,min_area=0):
    '''
    description : preprocess  input image to be black and white, and clear any noise from has area less than the
    min_area, using mean adaptive threshold
    :param im: the image to preprocess , np.array
    :param min_area: min area of object to remain in the image, int
    :return: preprocessed image black and white, np.array
    '''
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # change the image to gray scale
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV,11,2) # adaptive thresh mean method to get the image in black and white only

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # getting the contours

    #==================== clearing the image with min_area  =================#
    for cnt in contours:
        if cv2.contourArea(cnt)<min_area :
            [x, y, w, h] = cv2.boundingRect(cnt)
            thresh[y:y+h,x:x+w]=[0]
    thresh=cv2.bitwise_not(thresh)
    return thresh
def start_pre(image):
    out=preprocessing_image_to_black_and_white(image)
    out=cv2.cvtColor(out,cv2.COLOR_GRAY2BGR)
    return out
