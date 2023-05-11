def string_to_dict(string: str):
    string_dict = {}
    for letter in string:
        if letter not in string_dict:
            string_dict[letter] = 0
        string_dict[letter] += 1
    return string_dict


if __name__ == "__main__":
    str1 = "bbbbaaaacccaaaaaaddddddddccccccc"
    str2 = "coxinha"

    print(string_to_dict(str1))
    print(string_to_dict(str2))
