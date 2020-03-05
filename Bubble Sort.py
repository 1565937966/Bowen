a = []
temp =None
Numbers = int(input("Pls enter how many nnumbers you want to input: "))

for index in range(0, Numbers):
    print("pls enter the %d number: " % (index+1))
    number = int(input())
    a.append(number)

for outter in range(0, len(a)-1):
    for inner in range(0, len(a)-1):
        if a[inner] > a[inner+1]:
            # temp = a[inner]
            # a[inner] = a[inner+1]
            # a[inner+1] = temp
            a[inner], a[inner+1] = a[inner+1], a[inner]
print("The sort result is: ", a)
