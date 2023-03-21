LIST = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]


def find_lower(list):
    lower = list[0]
    for number in list:
        if lower > number:
            lower = number
    return lower


def find_lower2(list):
    return sorted(list)[0]


print(find_lower(LIST))
print(find_lower2(LIST))
