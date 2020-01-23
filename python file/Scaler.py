# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:26:24 2019

@author: 15659
"""


import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.style.use('ggplot')

y=[[1,2,3],[4,5,6]]
#x=np.random.randint(0,10,(3,3))
y=np.array(y,dtype=float)
print(y.shape)
data=pd.DataFrame(data=y,index=list("ab"),columns=list("ABC"))
print(data)
print(data.iloc[:,1:2])
print(data.iloc[:,[1,2]])
a="Bowen,hello,python"
a=a.split(",")
print(a)
Infor=dict()
Infor["name"]=a
print(Infor["name"][0])
'''
z_score=StandardScaler()
y_standard=z_score.fit_transform(y)
print(y_standard)
'''

'''
[[1. 2. 3.]
 [4. 5. 6.]]
[[-1. -1. -1.]
 [ 1.  1.  1.]]
np.random.seed(1)
df = pd.DataFrame({
    'x1': np.random.normal(0, 2, 10000),
    'x2': np.random.normal(5, 3, 10000),
    'x3': np.random.normal(-5, 5, 10000)
})
print(df.iloc[:,0].mean())
print(df.iloc[:,0].std())
print(df.iloc[:,1].mean())
print(df.iloc[:,1].std())
'''
