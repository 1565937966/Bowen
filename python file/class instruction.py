'''
class name():
    name="Python"
    def get_name(self):
        return self.name
'''
'''
class Rectangle():
    length=5
    width=4
    def get_Rec(self):
        print("The length is %d, the width is %d"%(self.length,self.width))
    def get_Area(self):
        print("Area is %d"%(self.length*self.width))
    def set_Rec(self):
        self.length=float(input("Length:"))
        self.width=float(input("Width:"))
        print("The length and width is %.2f %.2f"%(self.length,self.width))
'''

class ticket():
    us_price=100
    weekend_price=100*(1+100*1.2)
    kids_price=us_price/2
    kids_weekend=(100*(1+100*1.2))/2
    number_child=2
    number_adult=3
    def week_price(self,num_child,num_adult):
        self.num_child=num_child
        self.num_adult=num_adult
        print("Total price is %d"%(self.num_child*kids_price+self.num_adult*num_adult))
'''
class ticket():
    def _init_(self,weekend=False,child=False):
        self.expens=100
        if weekend==True:
            self.times=1.2
        else:
            sefl.times=1
        if child==True:
            self.discount=0.5
        else:
            self.discount=1
    def cal(self,number):
        self.number=number
        return(self.expens*self.times*self.discount*self.number)
'''
'''
class Ticket():
    week_price=100
    week_rate=1.2
    weekend_price=week_price*week_rate
    child_price=week_price/2
    child_weekend_price=weekend_price/2
    def __init__(self,num_child,num_adult):
        self.num_child=num_child
        self.num_adult=num_adult
        print("%dadult and %dchildren,total price is%d"%(self.week_price*self.num_adult,self.child_price*self.num_child,self.week_price*self.num_adult+self.child_price*self.num_child))
        
