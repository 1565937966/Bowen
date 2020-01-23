"""
def main():
    a = 10
    b = 20
    swap(a, b)
    print(a, b)


def swap(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)

a = 20
b = 10
a, b = b, a
print(a, b)
"""
a = 10
print("The address of a1 %d" % (id(a)))
a = 20
print("The address of a2 %d" % (id(a)))
