# Copyright : Vincent SAHLER, 2018

import cv2
import numpy as np

def isInto(_val, _min, _max):
    return _val <= _max and _min <= _val

def contrast(img, marge):
    h, w, c = img.shape # get image size (x, y, channels)
    result = np.zeros(h/2, w/2, c)
    bRbuffer = np.ones((6, 1), dtype=bool)
    bResult = np.ones((2, 3), dtype=bool)

    for _x in range(h/2):
        for _y in range(w/2):
            cPixels = [[img[_x*2, _y*2], img[_x*2+1, _y*2]], [img[_x*2, _y*2+1], img[_x*2+1, _y*2+1]]]
            for mX in range(2):
                for mY in range(3-mX):
