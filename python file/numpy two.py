# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:40:11 2019

@author: 15659
"""


import numpy as np

array_one = np.arange(0,11)


slice_of_arr = array_one

slice_of_arr[:] = 99

print(id(array_one))

print(id(slice_of_arr))

print("array_one:", array_one)

print("slice_of_arr", slice_of_arr)

#list_one = [1,2,3,4,5]

#list_two = list_one[0:3]

# print (list_two)

# id(list_one)
# id(list_two)