file = open("arquivo.txt", mode="w")
# ao abrir um arquivo para escrita, um novo arquivo é criado mesmo que
# ele já exista, sobrescrevendo o antigo.


file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")

# Não precisa da quebra de linha, pois esse é um comportamento padrão do print
print("Túlio 22", file=file)

LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file.writelines(LINES)

file.close()

# leitura
# file = open("arquivo.txt", mode="r")
# content = file.read()
# print(content)
# file.close()  # não podemos esquecer de fechar o arquivo

# leitura iteravel

file = open("arquivo.txt", mode="r")
for index, line in enumerate(file):
    if index > 0:
        name, age = line.split(" ")
        print(f"Nome: {name}, idade: {age}")
file.close()  # não podemos esquecer de fechar o arquivo
