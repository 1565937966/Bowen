def quick_sort(aList, start, end):
    if start >= end:
        return aList
    length = end
    mid_value = aList[start]
    high = length
    low = start
    while low < high:
        while low < high and aList[high] >= mid_value:
            high -= 1
        aList[low] = aList[high]
        while low < high and aList[low] < mid_value:
            low += 1
        aList[high] = a[low]
    aList[low] = mid_value
    left_end = low - 1
    right_start = low + 1
    return quick_sort(aList, start, left_end), quick_sort(aList, right_start, end)


if __name__ == "__main__":
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(a, 0, len(a)-1)
    print(a)