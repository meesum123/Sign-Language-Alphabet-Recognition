import csv
import numpy as np
import cv2
import numpy as np # linear algebra
import json
from matplotlib import pyplot as plt
from skimage import color
from skimage.feature import hog
from sklearn import svm
from sklearn.metrics import classification_report,accuracy_score
import os
import pandas as pd
import pickle
filename = "sign_mnist_test.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)

	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)


ppc = 14
hog_images = []
hog_features = []
labels = []
count = 1
image = np.zeros((28,28), np.uint8)
x = 0
y = 1
a = 1
b = 29
c = 0
count = 1
for row in rows:
    x = 0
    y = 1
    a = 1
    b = 29
    for c in range(0,28):
        image[x][:] = row[a:b]
        x = x+1
        a = b
        b = b + 28
    fd,hog_image = hog(image, orientations=8, pixels_per_cell=(ppc,ppc),cells_per_block=(1, 1),block_norm= 'L2',visualise=True)
    hog_images.append(hog_image)
    hog_features.append(fd)
    labels.append(row[0])


hog_features = np.array(hog_features)
labels = np.array(labels)
print(len(hog_features[0]))
print(len(labels))
filename = 'finalized_model_gridparams.sav'
loaded_model = pickle.load(open(filename, 'rb'))

result = loaded_model.score(hog_features, labels)
#result = loaded_model.predict(hog_features)
print(result)
