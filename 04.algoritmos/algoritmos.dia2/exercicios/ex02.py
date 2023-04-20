def find_even_numbers(n):
    count = 0
    return (
        (count + 1 if n % 2 == 0 else count) + find_even_numbers(n - 1)
        if n > 1
        else count
    )


print(find_even_numbers(10))
