import random

WORD_LIST = ["Paralelepipedo", "Estrutura", "Javascript", "Python"]


def guessing():
    word = random.choice(WORD_LIST)
    scrambled_word = "".join(random.sample(word, len(word)))
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
