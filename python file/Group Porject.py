# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:30:23 2019

@author: 15659
"""


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTree
data = pd.read_csv("C://Users//15659//Desktop//Sicentist_data.csv")
x = data.iloc[:,1:-1].values
y = data.iloc[:,-1].values
