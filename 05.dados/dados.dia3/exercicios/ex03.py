# Imagine que você esteja trabalhando em um e-commerce,
# e foi lhe dado a demanda de analisar um array de números inteiros que
# representam os produtos dessa empresa. Verifique quantos produtos formam
# boas combinações, ou seja, quando um produto é igual ao outro e seu índice
# é maior que o anterior. Esta combinação pode ser utilizada para modificar
# os produtos de uma página.


def find_matches(products: list):
    count = 0
    size = len(products)
    for i in range(size):
        next = i + 1
        count += products[next:].count(products[i])
    return count


def good_pairs(numbers):
    answer = 0
    i = 0
    size = len(numbers)
    for i in range(size):
        for j in range(i + 1, size):
            if numbers[i] == numbers[j]:
                answer += 1
    return answer


produtos = [1, 3, 1, 1, 1, 3]
print(find_matches(produtos))
print(good_pairs(produtos))

produtos = [1, 1, 2, 3]
print(find_matches(produtos))
