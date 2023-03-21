G = 2.50
A = 1.90


def calculate(litro, type):
    if type == "A":
        if litro < 20:
            return litro * (A - (A * 0.03))
        else:
            return litro * (A - (A * 0.05))

    if type == "G":
        if litro < 20:
            return litro * (G - (G * 0.04))
        else:
            return litro * (G - (G * 0.06))


print(calculate(1, "A"))
