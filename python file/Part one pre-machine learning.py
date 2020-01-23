#import data
import numpy as np
import pandas as pd
import matplotlib as plt

#from easygui import *
dataset=pd.read_csv("C://Users//15659//Desktop//python file//Data//Data.csv")
x=dataset.iloc[:,:3].values
y=dataset.iloc[:,3].values


#deal with missing data 

from sklearn.preprocessing import Imputer
imputer= Imputer(missing_values='NaN',strategy='mean',axis= 0)
#imputer=imputer.fit(x[:,1:3])为什么class.x返回的还是一个object .fit也是一个class?
#Imputer is a module
x[:,1:3]=imputer.fit_transform(x[:,1:3])

#deal with categorical variable

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
x[:,0]=labelencoder.fit_transform(x[:,0])

onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()



from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
array=[1,2,3,4]
#x=label.fit(array)
#y=label.transform(array)
y=label.fit_transform(array)

#Split data into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


#Making data in a same scale

from sklearn.preprocessing import StandardScaler
std=StandardScaler()
x_train=std.fit_transform(x_train)
x_test=std.fit_transform(x_test)


