def contains_duplicate(numbers):
    numbers.sort()
    for index, number in enumerate(numbers):
        start = index
        end = len(numbers) - 1
        count = 0
        while start <= end:
            if number == numbers[start]:
                count += 1
            elif number == numbers[end]:
                count += 1
            start += 1
            end -= 1
            if count >= 2:
                return True
    return False


# def contains_duplicate(numbers):
#     numbers.sort()
#     previous_number = "not a number"
#     for number in numbers:
#         if previous_number == number:
#             return True
#         previous_number = number

#     return False


# complexidade O(n)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 11, 12, 13]

print(contains_duplicate(numbers))
