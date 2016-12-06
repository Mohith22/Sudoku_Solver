import pylab as pl 
import numpy as np
import cv2

#Read Original Image Through WebCam
sudoku_original = cv2.imread('sudoku-2.png')
#Display Image On To Screen
cv2.imshow('Sudoku-1',sudoku_original)
cv2.waitKey(0)
cv2.destroyAllWindows()

