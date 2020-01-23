# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:14:34 2018

@author: 15659
"""

# Simple Linear Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# Preprocessing data

# import data use pandas
dataset = pd.read_csv("C://Users//15659//Desktop//CS//python file//Data//Salary_Data.csv")
x = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

x = x.reshape(-1, 1)  # or using x.reshape(30,1), that's to make the array become one coloumn
# print(x)
# checking if there is a missing value, if no, pass

# checking if there is a need to change categorical data using LabelEncoder or OneHotEncoder
# if no, pass
# cheching if there is a need to make satandard scale, if no, pass

# spliting the data into train and test set

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=0)

# Making prpgram to learn this model by using traning set
Regression = LinearRegression()
model=Regression.fit(x_train, y_train)

# To test this model by using testing set
y_predit = Regression.predict(x_test)

# visualizing the model

plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, Regression.predict(x_train))
plt.title("Experience VS Salary")
plt.xlabel("Year Experience")
plt.ylabel("Salary")
plt.show()

'''
plt.scatter(x_test, y_test, color="black")
plt.plot(x_test,Regression.predict(x_test))
plt.title("Test Set")
plt.xlabel("Year Experience")
plt.ylabel("Salary")
plt.show()
'''

'''
plt.scatter(x_test, y_test, color="black")
plt.plot(x_train,Regression.predict(x_train))
plt.title("Test Set")
plt.xlabel("Year Experience")
plt.ylabel("Salary")
plt.show()
'''

import statsmodels.formula.api as smf
x=np.append(arr=np.ones((30,1), dtype=float), values=x, axis=1)
x_opt=x[:,:2]
#print(x_opt[0,:])
regressor_ols=smf.OLS(endog=y, exog=x_opt).fit()
regressor_ols.summary()
regressor_ols.pvalues

model.intercept_
model.coef_




