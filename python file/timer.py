import time as t
class timer:
    def __init__(self):
        self.total=[]
        self.notice="Not start"
    def __repr(self):
        return self.notice
    def star(self):
        self.notice="Start!"
        self.begin=t.localtime()
    def stop(self):
        self.end=t.localtime()
        print("Finished")
    def sub(self):
        self.notice="The total is:"
        #for i in range(6):
            #self.total.append(self.end[i]-self.begin[i])
        self.notice+=str(self.end-self.begin)
        print(self.notice)
