import pylab as pl 
import numpy as np
import math
import Image
import pytesseract
from matplotlib import pyplot as plt
import cv2



SUDOKU_SIZE= 9


#Read Original Image Through WebCam
sudoku_original = cv2.imread('sudoku_4.png')

#Display Image On To Screen
  #cv2.imshow('Sudoku-2',sudoku_original)

#Convert Into Gray Scale From RGB Because Processing Of Image Is Done Only On Gray-Scale Images
sudoku_gray = cv2.cvtColor(sudoku_original,cv2.COLOR_BGR2GRAY)

#Detect The Lines (Edge Detection) - Adaptive Thresold Method
#The arguments for adaptiveThrehold Method Are Details Like Threshold Type , Size Of Pixel Neighbourhood etc.  (No need for us as of now)
sudoku_edge = cv2.adaptiveThreshold(sudoku_gray,255,1,1,15,9)

#Display Edge Detected Image
cv2.imshow('EdgeDetected-Sudoku',sudoku_edge)

#sudoku representation
sudoku = np.zeros((9,9))



#Below Code Is To Plot All The Grids Individually


x = 0
y = 0
'''
for i in range(9):
	y=0
	for j in range(9):
		cv2.imwrite('number.jpg',sudoku_edge[x:x+33,y+33])
		num = pytesseract.image_to_string(Image.open('number.jpg'))
		print num
		y = y+33
	x=x+33
'''


cv2.waitKey(0)
cv2.destroyAllWindows()

