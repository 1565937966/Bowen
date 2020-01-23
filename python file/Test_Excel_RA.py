# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:35:03 2019

@author: 15659
"""


import pandas

#Rows = 1
#data = pd.read_excel("C://Users//15659//Desktop//syllabus category.xlsx")
data = pandas.read_excel("C://Users//15659//Desktop//syllabus category.xlsx")
Links = data.iloc[1:, 0].values
Links_five =data.iloc[0:5,0].values
print(Links_five)

#print(data)

#print(data.head())
#print(data.info())
#data_type = data.info()


'''
content_example = data.iloc[0,:]
print(content_example)


Links = data.iloc[:,0].values
Links_holder = []
for link in Links:
    Links_holder.append(str(link))
Labs = data.iloc[:,6].values
for lab in Labs: # To make sure if true or false in Excel is valid in Python (0 false 1 true)
    Rows += 1
    if lab == 1 :
        print(Rows)
'''
#Links = data.iloc[2:3,0].values
#print(Links)
#print(type(Links))
'''
print(Links[0])
count = 0
University_name = data.iloc[1:,2]
University_name_holder = []
for item in University_name:
    University_name_holder.append(item)
print(University_name_holder)
'''


