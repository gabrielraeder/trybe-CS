from stack import Stack


def solve_expression(expr):
    stack = Stack()

    tokens_list = expr.split(" ")
    for token in tokens_list:
        if token == "+":
            # Sum operation
            result = stack.pop() + stack.pop()
            stack.push(result)
        elif token == "-":
            # Minus operation
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 - op2
            stack.push(result)
        elif token == "*":
            # multiply operation
            result = stack.pop() * stack.pop()
            stack.push(result)
        elif token == "/":
            # division operation
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 / op2
            stack.push(result)
        else:
            # add number operation
            stack.push(int(token))
    return int(stack.pop())


# A = 5, B = 10, C = 30

print("=" * 5)
# A + B - C / A -> 5 10 + 30 5 / -
print(solve_expression("5 10 + 30 5 / -"))  # 9
print("=" * 5)
# B + (A * C) / C * 2 -> 10 5 30 * 30 / 2 * +
print(solve_expression("10 5 30 * 30 / 2 * +"))  # 20
print("=" * 5)
# A * B - C + 4 * A - B -> 5 10 * 30 - 4 5 * 10 - +
print(solve_expression("5 10 * 30 - 4 5 * 10 - +"))  # 30
print("=" * 5)
# (A + C / B ) * (A + B) -> 30 10 / 5 + 5 10 + *
print(solve_expression("30 10 / 5 + 5 10 + *"))  # 120
print("=" * 5)
# 50 * B / 2 * 5 / A -> 50 10 * 2 / 5 * 5 /
print(solve_expression("50 10 * 2 / 5 * 5 /"))  # 250
print("=" * 5)
