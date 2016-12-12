import pylab as pl 
import numpy as np
import math
import Image
import pytesseract
from matplotlib import pyplot as plt
import cv2

#This function reads the text in the image
#num=pytesseract.image_to_string(Image.open('sample.png')) #comment it after running and try below one
img2=cv2.imread('sudoku_4.png')
img3=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img4=cv2.adaptiveThreshold(img3,255,1,1,15,9)
#img = cv2.fastNlMeansDenoising(img4,None,10,10,7,21)
cv2.imwrite('sudsam.jpg',img4)
num=pytesseract.image_to_string(Image.open('sudsam.jpg'))
print num

#When you run the below one : It is reading only some numbers and if i just send single grid (any one of 9*9 grids) it is not detecting it at all 
#So try to find solutions for these two problems

cv2.waitKey(0)
cv2.destroyAllWindows()