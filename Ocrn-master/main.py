from ocrn import dataset as ds
from ocrn import feature as ft
from ocrn import neuralnet as nt
import numpy as np
import cv2

print "Ocrn: Optical Character Recognition using Neural Network\nLatest version available at http://github.com/swvist\n"

n = nt.neuralnet(100,80,1)
print "Neural Network Initialized"

d = ds.dataset(100,1)
print "Training Data Set Initialized"

if d.generateDataSet():
	print "Training Data Set Generated"

if n.loadTrainingData(d.getTrainingDataset()):
	print "Training Data Set loaded"

number = cv2.imread("sudoku_edge.jpg")
cv2.imwrite('number.jpg',number[66:99,66:99])
num = cv2.imread('sudoku_edge.jpg')
x = n.activate(ft.feature.getImageFeatureVector(num))
print "\nThere is a high probability that the image is '"+str(unichr(x))+"'\n"

