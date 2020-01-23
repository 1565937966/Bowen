# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:42:59 2019

@author: 15659
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# get the data set

data_set = pd.read_csv("C://Users//15659//Desktop//CS//python file//Data//50_Startups.csv")
#data_set=pd.DataFrame(data_set, columns=["R&D Spend","Administration","Marketing Spend","State","Profit"] )
#print(data_set)
x = data_set.iloc[:,:4].values
#x=pd.DataFrame(x, columns=["R&D Spend","Administration","Marketing Spend","State"])
y = data_set.iloc[:,4].values
#y=pd.DataFrame(y, columns=["profit"])
#print(x)
#print(y)


label = LabelEncoder()
x[:, 3] = label.fit_transform(x[:, 3])
oneHotencoder = OneHotEncoder(categorical_features=[3])
x = oneHotencoder.fit_transform(x).toarray()

# Make sure avoid one dumy variable

x=x[:,1:]

###################################
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state=0)

regression = LinearRegression()
regression.fit(x_train, y_train)

# Test the module

y_predit = regression.predict(x_test)
import statsmodels.formula.api as smf
x=np.append(arr=np.ones((50,1),dtype=float), values=x, axis=1)
regressor=smf.OLS(y,x).fit()
regressor.summary()
attributes= x[:,[0,1,2,3,4,5]]
def backward_elimination(X,y):
    NumOfVar=len(X[0])
    sl=0.05
    for i in range(0, NumOfVar):
        regressor=smf.OLS(y,X).fit()
        p_values=regressor.pvalues
        Max_value=max(p_values).astype(float)
        if Max_value>sl:
            for index in range(0, NumOfVar-i):
                if p_values[index].astype(float)==Max_value:
                    X=np.delete(X,index,1)
    print(regressor.summary())
    print(regressor.params)
    return X

new_attr=backward_elimination(attributes,y)
                





