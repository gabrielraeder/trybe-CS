def separate_by_initial_letter(words: list):
    separated = {}
    for word in words:
        if word[0].lower() not in separated:
            separated[word[0].lower()] = [word]
        else:
            separated[word[0].lower()].append(word)
    return separated


words = [
    "Ana",
    "ama",
    "Joao",
    "que",
    "ama",
    "Jose",
    "mais",
    "Jose",
    "nao",
    "ama",
    "Ana",
]

print(separate_by_initial_letter(words))
