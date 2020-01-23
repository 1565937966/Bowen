def Fun(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
n=int(input("输入一个整数:"))
Fun(n)
print("%d 的阶乘是:%d" % (n,Fun(n)))
