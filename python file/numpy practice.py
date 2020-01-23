# -*- coding: utf-8 -*-
"""
Created on Wed May 29 00:21:34 2019

@author: 15659
"""


import numpy as np
import matplotlib.pyplot as plt

x,y=np.meshgrid(np.arange(0,5,1),np.arange(0,5,1))
z=np.array([[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]])
'''
print(x)
print(y)
plt.plot(x, y)
'''

LineSpace = np.linspace(0,5,4) # use the diffrence between 0,5 divided by 4-1 because there are 3 intervals
plt.contourf(x,y,z)

