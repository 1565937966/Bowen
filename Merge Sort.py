def division(array):
    length = len(array)

    if length == 1:
        return array
    split = length // 2
    left = division(array[:split])
    right = division(array[split:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_point = 0
    right_point = 0
    while left_point<len(left) and right_point<len(right):
        if left[left_point] < right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1

    result += left[left_point:]
    result += right[right_point:]
    return result


if __name__ == "__main__":
    a = [6, 2, 3, 5]
    print(division(a))