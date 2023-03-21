def media(list):
    total = 0
    for item in list:
        total += item
    return total / len(list)


print(media([10, 9, 10, 9, 10]))
