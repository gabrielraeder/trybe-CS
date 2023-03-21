def boomerang(elements: list) -> str:
    reverse = elements[::-1]  # elements.reverse()
    boomerang = elements[0:-1] + reverse
    for item in boomerang:
        print(item, end=" ")
    print("\n")
    return " ".join(map(str, boomerang))


list = [0, 1, 2, 3]

print(boomerang(list))
