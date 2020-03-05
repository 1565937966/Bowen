def division(array):
    length = len(array)

    if length == 1:
        return array
    split = length // 2
    left = division(array[:split])
    right = division(array[split:])
    return left, right


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    print(division(a))