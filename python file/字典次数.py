Infor=dict()
counter=dict()
number=0
for i in range(3):
    x=input("Insert a name: ")
    y=input("Insert a number: ")
    Infor[x]=y
    counter[x]=0
for j in range(len(Infor)):
    name=input("insert a name: ")
    if name in counter:
        counter[name]+=1
for each in counter:
    print("%s:%s"%(each,counter[each]))
    





    
