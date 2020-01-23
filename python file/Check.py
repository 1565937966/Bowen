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
        print("child price is %d,adult price is %d"%(self.num_child*self.kids_price,self.num_adult*self.us_price))
