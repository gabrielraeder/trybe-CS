LINES = [
    "Marcos 10\n",
    "Felipe 4\n",
    "José 6\n",
    "Ana 10\n",
    "Maria 9\n",
    "Miguel 5\n",
]

with open("grades.txt", "w") as file:
    file.writelines(LINES)

with open("grades.txt", "r") as file:
    with open("reproved.txt", "w") as second_file:
        for line in file:
            name, grade = line.split(" ")
            if int(grade) < 6:
                second_file.write(f"{name}\n")

print(file.closed)
print(second_file.closed)
