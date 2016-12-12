import random
import matplotlib.pyplot as plt
import pylab as pl
from sklearn.datasets import load_digits
from sklearn import ensemble

digits = load_digits()

n_samples = len(digits.images)
x = digits.images.reshape((n_samples,-1))
y = digits.target

print digits.images
print n_samples
print x
print y

sample_index = random.sample(range(len(x)),len(x)/5)
valid_index = [i for i in range(len(x)) if i not in sample_index]

#Sample and validation images
sample_images=[x[i] for i in sample_index]
valid_images=[x[i] for i in valid_index]

#Sample and validation targets
sample_target=[y[i] for i in sample_index]
valid_target=[y[i] for i in valid_index]

#Using the Random Tree Classifier
classifier = ensemble.RandomForestClassifier()

#Fit model with sample data
classifier.fit(sample_images, sample_target)

#Attempt to predict validation data
score=classifier.score(valid_images, valid_target)
print 'Random Tree Classifier:\n' 
print 'Score\t'+str(score)

#number = cv2.imread('sudoku_edge.jpg')
#num = number[66:99,66:99]


#print classifier.predict()