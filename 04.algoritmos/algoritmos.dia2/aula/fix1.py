def soma_recursiva(n):
    return n + soma_recursiva(n - 1) if n > 0 else n


print(soma_recursiva(5))  # 5 + 4 + 3 + 2 + 1
