double_or_triple = {i: i * 2 if i % 2 == 0 else i * 3 for i in range(3, 21)}


print(double_or_triple)

double = {i: i * 2 for i in range(3, 21)}

for key in double.keys():
    if key % 2 != 0:
        double[key] = key * 3


print(double)
