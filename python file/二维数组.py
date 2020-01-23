a=[]
x=int(input("Pls enter the rows:"))
y=int(input("Pls enter the colums:"))
for i in range(0,x):
    a.append([])
    for j in range(0,y):
        a[i].append(i*j)
for i in range (0,x):
    print(str(a[i]))
    
