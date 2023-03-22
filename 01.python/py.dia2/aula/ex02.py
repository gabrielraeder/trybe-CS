n = input("digite seus numeros: ").strip()


def sum(numbers: str):
    listing = numbers.split(" ")
    total = 0
    for number in listing:
        if number.isdigit():
            total += int(number)
        else:
            return f"Erro ao somar valores, {number} é um valor inválido"
    return f"Total = {total}"


# print(sum(n))
