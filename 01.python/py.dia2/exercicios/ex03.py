import random

WORD_LIST = ["Paralelepipedo\n", "Estrutura\n", "Javascript\n", "Python\n"]

with open("words.txt", "w") as file:
    file.writelines(WORD_LIST)


def word_picker():
    with open("words.txt", "r") as file:
        all_words = []
        for line in file:
            all_words.append(line)
        word = random.choice(all_words).strip()
    scrambled_word = "".join(random.sample(word, len(word)))
    return word, scrambled_word


def guessing():
    word, scrambled_word = word_picker()
    counter = 0
    print(f"descubra a seguinte palavra:\n {scrambled_word}")
    while counter < 3:
        counter += 1
        guess = input(f"{counter}º chute: ").capitalize()
        if word != guess:
            print("tente novamente.")
        elif word == guess:
            print("Parabéns!")
            break
    if counter == 3:
        print("Falhou!")


guessing()
