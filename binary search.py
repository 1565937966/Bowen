def Binary_search(data, alist, first, last):
    if first - last > 0:
        return False
    mid_index = (first+last)//2
    left = mid_index - 1
    right = mid_index + 1
    if data < alist[mid_index]:
        return Binary_search(data, alist, first, left)
    elif data == alist[mid_index]:
        return True
    else:
        return Binary_search(data, alist, right, last)


'''
length = len(alist)
    if length > 0:
        mid_index = length // 2
        if data < alist[mid_index]:
            return Binary_search(data, alist[:mid_index])
        elif data == alist[mid_index]:
            return True
        else:
            return Binary_search(data, alist[mid_index + 1:])
    else:
        return False
'''


if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]
    print(Binary_search(2, a, 0, len(a)))


