# from collections import Counter


class Estatistica:
    @classmethod
    def media(cls, numbers: list[int]):
        total = 0
        for number in numbers:
            total += number
        return total / len(numbers)

    @classmethod
    def mediana(cls, numbers: list[int]):
        numbers.sort()
        result = 0
        if len(numbers) % 2 != 0:
            index = int((len(numbers) - 1) / 2 + 1)
            result = numbers[index]
        else:
            index = int(len(numbers) / 2)
            result = (numbers[index] + numbers[index + 1]) / 2
        return result

    @classmethod
    def moda(cls, numbers):
        dicionario = {}
        for number in numbers:
            if number not in dicionario:
                dicionario[number] = 0
            dicionario[number] += 1
        result = sorted(
            dicionario.items(), key=lambda item: item[1], reverse=True
        )[0][0]
        # numb, _ = Counter(numbers).most_common()[0]
        # print(Counter(numbers))
        return result


impar = [2, 5, 7, 3, 10]
par = [2, 2, 3, 4, 5, 6]

print(Estatistica.moda(par))
