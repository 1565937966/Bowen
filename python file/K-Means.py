# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:46:27 2019

@author: 15659
"""


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs
sns.set()
x,y = make_blobs(n_features=3,n_samples=300, centers=4, random_state=0,cluster_std=0.60)
# What is the relationship between x and y by using this class or function?

#print(x)
print(x.shape)
print(y.shape)
print(len(y))

'''
plt.scatter(x[:,0],x[:,1])
from sklearn.cluster import KMeans
KM = KMeans(4)
KM.fit(x)
y_kmeans = KM.predict(x)
print(y_kmeans.shape)
print(y_kmeans)
print(y)
plt.scatter(x[:,0],x[:,1],c=y, cmap='rainbow')
'''
# from mpl_toolkits.mplot3d import axes3d 
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
# ax = fig.add_subplot(projection='3d')
ax.scatter(x[:,0],x[:,1],x[:,2],c=y, cmap='rainbow')
ax.set_xlabel('feature one')
ax.set_ylabel('feature two')
ax.set_zlabel('feature three')
plt.show()