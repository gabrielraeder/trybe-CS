def fizzbuzz(n):
    new_list = []
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            new_list.append("FizzBuzz")
        elif n % 3 == 0 and n % 5 != 0:
            new_list.append("Fizz")
        elif n % 3 != 0 and n % 5 == 0:
            new_list.append("Buzz")
        else:
            new_list.append(n)
    return new_list


if __name__ == "__main__":
    print(fizzbuzz(30))
