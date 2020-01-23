# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:58:57 2019

@author: 15659
"""


import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split 
# this is a new version for splitting the train and test set
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

# import the data 
data_set = pd.read_csv("C://Users//15659//Desktop//CS//python file//Data//Position_Salaries.csv")

x=data_set.iloc[:,1].values.reshape(-1,1)
y=data_set.iloc[:,2].values.reshape(-1,1)

# fit the data into simple linear regression the first

linear_regressor = LinearRegression()
linear_regressor.fit(x, y)

# visualization of linear regression

plt.scatter(x,y,color="red")
plt.plot(x, linear_regressor.predict(x))
plt.title("Level VS Salary")
plt.xlabel("Level")
plt.ylabel("($)Salary")
plt.show()

# create the polynomial features

ploy_feature = PolynomialFeatures(degree=3)
x_ploy = ploy_feature.fit_transform(x)
ploy_regressor = LinearRegression()
ploy_regressor.fit(x_ploy, y)# fie into the ploynomial regression

# vasiualization of polynomial regression

plt.scatter(x,y,color="red")
plt.plot(x, ploy_regressor.predict(x_ploy))
plt.title("Level VS Salary")
plt.xlabel("Level")
plt.ylabel("($)Salary")
plt.show()

# To predict accurate result for exactly number

linear_regressor.predict(6.5)

test=ploy_feature.fit_transform(6.5)

ploy_regressor.predict(ploy_feature.fit_transform(9.5))

# SVR can't dealt with scale by itself
svr_regressor=SVR(C=1.0,kernel="rbf")# linear, poly , rbf
x_score = StandardScaler()
y_score=StandardScaler()
x=x_score.fit_transform(x)
y=y_score.fit_transform(y)
svr_regressor.fit(x,y)
target = x_score.transform(np.array([[6.5]]))
pre = y_score.inverse_transform((svr_regressor.predict(target)))

plt.scatter(x,y,color="red")
plt.plot(x, svr_regressor.predict(x))
plt.title("Level VS Salary")
plt.xlabel("Level")
plt.ylabel("($)Salary")
plt.show()






