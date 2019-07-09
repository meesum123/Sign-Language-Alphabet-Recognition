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
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC


filename = "sign_mnist_train.csv"

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


filename = "sign_mnist_train.csv"
ppc = 14
hog_images = []
hog_features = []
labels = []
path = "Dataset/allimages"
dirs = os.listdir(path)
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
param_grid = {'C':[1,10,100,1000],'gamma':[1,0.1,0.001,0.0001], 'kernel':['linear','rbf']}
grid = GridSearchCV(SVC(),param_grid,refit = True, verbose=2)
#clf = svm.SVC()
hog_features = np.array(hog_features)
labels = np.array(labels)
#data_frame = np.hstack((hog_features,labels))
#np.random.shuffle(data_frame)
print("starting training")
#clf.fit(hog_features,labels)
grid.fit(hog_features,labels)
print("finished training")
print(grid.best_params_)
filename = 'finalized_model_gridparams.sav'
pickle.dump(grid, open(filename, 'wb'))
print("saved model to disk")
