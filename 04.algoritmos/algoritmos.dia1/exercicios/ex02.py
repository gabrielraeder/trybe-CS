import random


def random_averages(n):
    averages = []
    for _ in range(100):
        average = 0
        for _ in range(n):
            average += random.randrange(1, n)
            average = average / n
            averages.append(average)
    return averages


# complexidade O(n^2)
