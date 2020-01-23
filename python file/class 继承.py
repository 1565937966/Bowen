import math as m
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Line:
    def __init__(self,p1,p2):
        self.x=p1.getX()
        self.y=p1.getY()
        self.x2=p2.getX()
        self.y2=p2.getY()
    
    def len(self):

        return m.sqrt(pow(self.x-self.x2,2)+pow(self.y-self.y2,2))
    
    
