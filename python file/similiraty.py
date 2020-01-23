# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:16:37 2019

@author: 15659
"""

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# brand type function price 
Person_One_Two = ["Dior makeup white 200 Chanel makeup white 250 Nars makeup wet 180","Amani makeup white 200 Chanel makeup white 250 SK2 makeup wet 300" ]
vector = CountVectorizer()
matrix = vector.fit_transform(Person_One_Two)
similarity = cosine_similarity(matrix)
print(similarity)
Person_One=["Dior makeup white 200 Chanel makeup white 250 Nars makeup wet 180"]
#sim_list = list(enumerate(similarity))

#text = ['you both brain are good','your left brain is better','your right brain is better']

#for i in range (0,5):
'''
random.seed()
index = random.randint(0,2)
print(text[index])
'''