# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:04:26 2018

@author: 15659
"""
class People:
	def __init__(self,name,color,gender):
		self.name=name
		self.color=color
		self.gender=gender
	def Name(self):
		return self.name
	def Color(self):
		return self.color
	def Gender(self):
		return self.gender
class Person():
	def __init__(self,game):
		#super.__subclasses__(People)
		self.game=game
	def Game(self):
		return self.game
