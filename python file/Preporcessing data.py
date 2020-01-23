# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:45:33 2018

@author: 15659
"""
# import data

import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.preprocessing import Imputer 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("C://Users//15659//Desktop//CS//python file//Data//Data.csv")
x = dataset.iloc[:, :3].values
y = dataset.iloc[:, 3].values


# deal with missing data


imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
# Imputer is a module
x[:, 1:3] = imputer.fit_transform(x[:, 1:3])

# deal with categorical variable


label_encoder = LabelEncoder()
x[:, 0] = label_encoder.fit_transform(x[:, 0])

onehot_encoder = OneHotEncoder(categorical_features=[0])
x = onehot_encoder.fit_transform(x).toarray()
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)
print(x)



from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
array=[1,2,3,4]
#x=label.fit(array)
#y=label.transform(array)
y=label.fit_transform(array)


# Split data into training set and test set


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Making data in a same scale


z_score = StandardScaler()
x_train = z_score.fit_transform(x_train)
x_test = z_score.transform(x_test)
print(x_train, x_test)



