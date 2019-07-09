# importing csv module
import csv
import numpy as np
import cv2

# csv file name
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

	# get total number of rows
	#print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
"""
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
	# parsing each column of a row
	for col in row:
		print("%10s"%col),
	print('\n')
"""
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
    print(row[0])
    cv2.imwrite("Dataset/allimages/sign" + str(count) + ".jpg", image)
    if(row[0] == "0"):
        cv2.imwrite("Dataset/0/sign" + str(count) + ".jpg",image)
    if(row[0] == "1"):
        cv2.imwrite("Dataset/1/sign" + str(count) + ".jpg",image)
    if(row[0] == "2"):
        cv2.imwrite("Dataset/2/sign" + str(count) + ".jpg",image)
    if(row[0] == "3"):
        cv2.imwrite("Dataset/3/sign" + str(count) + ".jpg",image)
    if(row[0] == "4"):
        cv2.imwrite("Dataset/4/sign" + str(count) + ".jpg",image)
    if(row[0] == "5"):
        cv2.imwrite("Dataset/5/sign" + str(count) + ".jpg",image)
    if(row[0] == "6"):
        cv2.imwrite("Dataset/6/sign" + str(count) + ".jpg",image)
    if(row[0] == "7"):
        cv2.imwrite("Dataset/7/sign" + str(count) + ".jpg",image)
    if(row[0] == "8"):
        cv2.imwrite("Dataset/8/sign" + str(count) + ".jpg",image)
    if(row[0] == "9"):
        cv2.imwrite("Dataset/9/sign" + str(count) + ".jpg",image)
    if(row[0] == "10"):
        cv2.imwrite("Dataset/10/sign" + str(count) + ".jpg",image)
    if(row[0] == "11"):
        cv2.imwrite("Dataset/11/sign" + str(count) + ".jpg",image)
    if(row[0] == "12"):
        cv2.imwrite("Dataset/12/sign" + str(count) + ".jpg",image)
    if(row[0] == "13"):
        cv2.imwrite("Dataset/13/sign" + str(count) + ".jpg",image)
    if(row[0] == "14"):
        cv2.imwrite("Dataset/14/sign" + str(count) + ".jpg",image)
    if(row[0] == "15"):
        cv2.imwrite("Dataset/15/sign" + str(count) + ".jpg",image)
    if(row[0] == "16"):
        cv2.imwrite("Dataset/16/sign" + str(count) + ".jpg",image)
    if(row[0] == "17"):
        cv2.imwrite("Dataset/17/sign" + str(count) + ".jpg",image)
    if(row[0] == "18"):
        cv2.imwrite("Dataset/18/sign" + str(count) + ".jpg",image)
    if(row[0] == "19"):
        cv2.imwrite("Dataset/19/sign" + str(count) + ".jpg",image)
    if(row[0] == "20"):
        cv2.imwrite("Dataset/20/sign" + str(count) + ".jpg",image)
    if(row[0] == "21"):
        cv2.imwrite("Dataset/21/sign" + str(count) + ".jpg",image)
    if(row[0] == "22"):
        cv2.imwrite("Dataset/22/sign" + str(count) + ".jpg",image)
    if(row[0] == "23"):
        cv2.imwrite("Dataset/23/sign" + str(count) + ".jpg",image)
    if(row[0] == "24"):
        cv2.imwrite("Dataset/24/sign" + str(count) + ".jpg",image)
    if(row[0] == "25"):
        cv2.imwrite("Dataset/25/sign" + str(count) + ".jpg",image)
    count = count + 1


cv2.imshow("Input", image)
cv2.waitKey(0)
