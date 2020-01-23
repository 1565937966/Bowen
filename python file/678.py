def function(n):
    n1=1
    n2=1
    k=0
    while (n-2)>0:
        k=n2+n1
        n1=n2
        n2=k
        n=n-1

    return k
n=int(input("输入一个数字:"))
a=function(n)
print("结果是:",a)

    
