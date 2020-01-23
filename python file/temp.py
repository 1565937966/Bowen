# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import data
import numpy as np
import pandas as pd
import matplotlib as plt
dataset=pd.read_csv("C://Users//15659//Desktop//python file//Data//Data.csv")
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,3]
#deal with missing data 

from sklearn.preprocessing import Imputer
imputer= Imputer(missing_values='Nan',strategy='mean',axis= 0)
imputer=imputer.fit(x[:,2:3])





