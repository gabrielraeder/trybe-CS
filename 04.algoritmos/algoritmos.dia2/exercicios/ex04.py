def recursive(a: int, b: int, mdc: int):
    if a % mdc == 0 and b % mdc == 0:
        return mdc
    else:
        return recursive(a, b, mdc - 1)


def mdc(a: int, b: int):
    return recursive(a, b, min([a, b]))


# def mdc(a, b):
#     if b == 0:
#         return a
#     return mdc(b, a % b)


print(mdc(8, 100))
