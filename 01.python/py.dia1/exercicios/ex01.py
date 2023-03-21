def find_biggest_number(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return "Valores Iguais."


print(find_biggest_number(21, 2))
