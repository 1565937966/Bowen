import random
number=random.randint(1,10)
user_name=input("Pls enter your name:")
print("Hello,"+user_name)
guess=int(input("Guess a number:"))
count=1
while guess!=number:
    if guess>number:
        print("Higher!")
        guess=int(input("Try again:"))
        count+=1
    if guess<number:
        print("Lower!")
        guess=int(input("Try again:"))
        count+=1
    if guess==number:
        print("You are right! You have tried %d times"%(count))
        
        
    

