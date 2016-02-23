#!/usr/bin/python3.5

import numpy as np
import cv2 as cv
import sys
import math


if __name__ == '__main__':
    cam0 = cv.VideoCapture( 0 )
    cam1 = cv.VideoCapture( 1 )

    while True:
        n, frame0  = cam0.read()
        n, frame1  = cam1.read()

        small1 = cv.resize(frame1, (0,0), fx=0.5, fy=1) 
        vis = np.concatenate((frame0, small1), axis=1)

        cv.imshow( 'frame', vis )
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cam0.release()
    cam1.release()
    cv.destroyAllWindows()
