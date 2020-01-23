class ticket():
    def __init__(self,weekend=False,child=False):
        self.exp=100
        if weekend==True:
            self.times=1.2
        else:
            self.times=1
        if child==True:
            self.discount=0.5
        else:
            self.discount=1
    def cal(self,num):
        return self.exp*self.times*self.discount*num
    
            
