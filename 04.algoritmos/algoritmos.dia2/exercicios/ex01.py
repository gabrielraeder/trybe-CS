def find_even_numbers(n):
    count = 0
    for number in range(1, n + 1):
        if number % 2 == 0:
            count += 1
    return count


print(find_even_numbers(10))
