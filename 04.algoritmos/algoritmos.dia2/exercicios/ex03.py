def max_number(numbers: list):
    size = len(numbers)
    if size == 1:
        return numbers[0]
    else:
        max = numbers[size - 1]
        if max_number(numbers[: size - 1]) > max:
            return max_number(numbers[: size - 1])
        return max


print(max_number([1, 15, 11, 40, 10, 4]))
