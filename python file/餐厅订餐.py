# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:14:39 2018

@author: 15659
"""


from urllib import request as r
import re
from bs4 import BeautifulSoup as bs
response=r.urlopen("http://oregonstate.edu")
html=response.read().decode('utf-8')
html_soup=bs(html,'html.parser')
#print(html_soup)
a=html_soup.find_all(href=re.compile('oregonstate'))
#if the target is tag, use find_all('tagname')
#if the target is artribute, use find_all(artribute=re.compile(' '))
for each in a:
    print(each.name)+each['href'])#each.name is the name of tag, not artribute
