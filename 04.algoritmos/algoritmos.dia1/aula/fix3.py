def sum_arrays(array1, array2, array3):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f"Array 1: {number1}")
        for number2 in array2:
            print(f"Array 2: {number2}")
            for number3 in array3:
                print(f"Array 3: {number3}")
                result.append(number1 + number2 + number3)
                number_of_iterations += 1

    print(f"{number_of_iterations} iterações!")
    return result


meu_array = list(range(1, 100))

sum_arrays(meu_array, meu_array, meu_array)

# time python3 meu_programa.py
