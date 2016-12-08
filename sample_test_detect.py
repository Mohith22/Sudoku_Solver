import pylab as pl 
import numpy as np
import math
import Image
import pytesseract
from matplotlib import pyplot as plt
import cv2

#This function reads the text in the image
num=pytesseract.image_to_string(Image.open('sample.png')) #comment it after running and try below one
#num=pytesseract.image_to_string(Image.open('sudoku_4.png'))
print num

#When you run the below one : It is reading only some numbers and if i just send single grid (any one of 9*9 grids) it is not detecting it at all 
#So try to find solutions for these two problems
cv2.waitKey(0)
cv2.destroyAllWindows()