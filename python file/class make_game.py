import random as r
limit_x=[0,10]
limit_y=[0,10]
class Turtle():
    def __init__(self):
        self.power=100
        self.x=r.randint(limit_x[0],limit_x[1])
        self.y=r.randint(limit_y[0],limit_y[1])
    def move(self):
        self.x=self.x+r.choice([-1,1,-2,2])
        self.y=self.y+r.choice([-1,1,-2,2])
        if self.x<limit_x[0]:
            self.x=limit_x[0]-(self.x-limit_x[0])
        elif self.x>limit_x[1]:
            self.x=limit_x[1]-(self.x-limit_x[1])
        elif self.y<limit_y[0]:
            self.y=limit_x[0]-(self.y-limit_y[1])
        elif self.y>limit_y[1]:
            self.y=limit_y[1]-(self.y-limit_y[1])
        else:
            self.power-=1
            return (self.x,self.y)
    def eat(self):
        def Power(self):
            self.power+=20
            if self.power>100:
                self.power=100
class Fish():
    def __init__(self):
        self.x=r.randint(limit_x[0],limit_x[1])
        self.y=r.randint(limit_y[0],limit_y[1])
    def move(self):
        self.x=self.x+r.choice([-1,1])
        self.y=self.y+r.choice([-1,1])
        if self.x<limit_x[0]:
            self.x=limit_x[0]-(self.x-limit_x[0])
        elif self.x>limit_x[1]:
            self.x=limit_x[1]-(self.x-limit_x[1])
        elif self.y<limit_y[0]:
            self.y=limit_x[0]-(self.y-limit_y[1])
        elif self.y>limit_y[1]:
            self.y=limit_y[1]-(self.y-limit_y[1])
        else:
            return (self.x,self.y)
turtle=Turtle()
new_fish=Fish()
fish=[]
for i in range(10):
    fish.append(new_fish.move())
    if len(fish)!=0:
        
    

        
