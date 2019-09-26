# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:42:27 2019

@author: shero
Flatland Performance
"""
"""import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.get_backend()

X_train = np.array([[1,1],[2,2.5],[3,1.2],[5.5,6.3],[6,9],[7,6]])
Y_train = ['red', 'red', 'red', 'blue', 'blue', 'blue']

print(X_train[5,0])
print(X_train[:,1])


X_test = np.array([3,4])

plt.figure()
plt.scatter(X_train[:,0], X_train[:,1], s = 170, color = Y_train[:])
plt.scatter(X_test[0], X_test[1], s = 170, color = 'green')

def dist(x,y):
    return np.square(np.sum((x-y)**2)) exmp: x = [1,1]
                                                 y = [3,4]
                                                 x - y = [-2,-3]
                                                 (x- y)**2 = [4,9]
                                                 np.sum((x-y)**2) = 13
                                                 np.square(np.sum((x-y)**2)) = 3.60
                                                 
                                                 
distance = np.zeros(len(X_train))   # create an empty array
for i in range (len(X_train)):      
    distance[i] = dist(X_train[i], X_test)  # check the distance between each dot with for loop
print(distance)"""

import matplotlib """ Unsupervised Learning"""
import numpy as np
import matplotlib.pyplot as plt
matplotlib.get_backend()

from sklearn import datasets
digits = datasets.load_digits()

print(digits.images[0])

plt.figure()
plt.imshow(digits.images[0], cmap = plt.cm.gray_r, interpolation = 'nearest') # to show an image
plt.show()

print(digits.target[0]) # print it`s value here it`s "0"

X_train = digits.data[0:10]
Y_train = digits.target[0:10]
X_test = digits.data[345]

 





