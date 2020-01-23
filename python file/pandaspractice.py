# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 23:44:30 2019

@author: 15659
"""


import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.preprocessing import Imputer 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data_set = pd.read_csv("C://Users//15659//Desktop//CS//python file//Data//Data.csv")


# use pandas to deal with missing value

data_set["Age"] = data_set["Age"].fillna(data_set["Age"].mean())
#data_set["Salary"] = data_set["Salary"].fillna(data_set["Salary"].mean())
#print(data_set["Age"])

# To find the features, which are columns name
attr = data_set.columns

# Get a new features or columns in dataframe
def Combined_Features(data):
    try:
        return data["Country"]+" "+ str(data["Age"])
    except:
        print ("Error", data)


# Don't neet to input the paramaters for this lamda expression, because data_set.apply has already input the paramaters for us
# data_set["combined_features"] =data_set.apply(lambda data:data["Country"]+" "+ str(data["Age"]), axis=1)
data_set["combined_features"] = data_set.apply(Combined_Features, axis=1)

print(data_set["Age"])


