# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:02:25 2019

@author: 15659
"""


import numpy as np

new_list = [1,2,3,4]

new_array = np.array(new_list)

new_list2 = [2,3,4,5]

# new_array2 = np.array(new_list,new_list2) This's not legal

list_comb = [new_list,new_list2]

new_array2 = np.array(list_comb)

zero_array = np.zeros(5,dtype=int) # change dtype to whatever you want

arange_array = np.arange(0,10,2) 

random_array = np.random.randint(0,10,size=5) # create a random array

eye_array = np.eye(3)

eye_array2 = np.eye(3,k=1)


