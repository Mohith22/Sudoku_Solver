import pylab as pl 
import numpy as np
import math
import Image
import pytesseract
from matplotlib import pyplot as plt
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	cv2.imwrite('sam.jpg',gray)
	num=pytesseract.image_to_string(Image.open('sam.jpg'))
	print num
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()