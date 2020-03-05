def shell_sort(aList):
    length = len(aList)
    step = length//2-1
    while step > 0:
        for j in range(step, length):
            i = j
            while i > 0:
                if aList[i] < aList[i-step]:
                    aList[i], aList[i-step] = aList[i- step], aList[i]
                    i -= step
                else:
                    break
        step = step //2
    return aList


if __name__ == "__main__":
    a = [3, 5, 4, 1, 0]
    print(shell_sort(a))





