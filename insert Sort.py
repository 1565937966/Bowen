def insert_sort(aList):
    length = len(aList)
    control = length - 1

    while length - control < length:
        index = length - control
        for i in range(index, 0, -1):
            if aList[i] < aList[i-1]:
                aList[i - 1], aList[i] = aList[i], aList[i - 1]

        control -= 1
    return aList


if __name__ == "__main__":
    a = [3, 5, 4, 1, 0]
    print(insert_sort(a))