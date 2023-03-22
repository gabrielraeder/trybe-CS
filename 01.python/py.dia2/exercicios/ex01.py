def name_printer(name: str):
    length = len(name)
    for i in range(length):
        print(name)
        name = name.rstrip(name[-1])


if __name__ == "__main__":
    name = input("Digite um nome: ").upper()
    name_printer(name)
