import random
number=random.randint(1,10)
while True:
    try:
        guess=int(input("insert a number:"))
    except ValueError as reason:
        print("insert wrong:"+str(reason))
        #if 'guess' in locals(): #有这个表达式的话guess这个变量就不会消失
        #否则需要重新定义guess变量 eg:
        #if guess!=number:NameError: name 'guess' is not defined
    if guess!=number:
        guess=int(input("Try again:"))
        print("Wrong")
    else:
        break
        
