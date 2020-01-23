# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:23:11 2019

@author: 15659
"""


# import the modules that we might need to use

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler


data_set = pd.read_csv("C://Users//15659//Desktop//CS//python file//Data//Position_Salaries.csv")
x = data_set.iloc[:,1].values.reshape(-1,1)
y = data_set.iloc[:,2].values.reshape(-1,1)


model=DecisionTreeRegressor(max_depth = 5)
model.fit(x, y)

'''
X_std = StandardScaler()
y_std = StandardScaler()

x = X_std.fit_transform(x)
y = y_std.fit_transform(y)
'''

new_xarray=np.arange(0,10,0.1).reshape(-1,1)
plt.scatter(x,y)
plt.plot(new_xarray,model.predict(new_xarray))
plt.title("Decision Tree Regression")
plt.xlabel("Salary")
plt.ylabel("Level")

from sklearn.tree import export_graphviz
import graphviz 
dot_data = export_graphviz(model, out_file=None, feature_names =["level"], class_names=model.classes_,filled=False, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("new postion level and salary_max5")
#graph.save("C://Users//15659//Desktop//DecisionTree Node//new postion level and salary.pdf")


