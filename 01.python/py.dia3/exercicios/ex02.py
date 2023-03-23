convert = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9,
}


def expression_to_number(exp: str) -> str:
    number = ""
    for char in exp:
        if char.upper().isalpha():
            for key, value in convert.items():
                if char.upper() in key:
                    number += str(value)
        else:
            number += char
    return number


if __name__ == "__main__":
    print(expression_to_number("1-HOME-SWEET-HOME"))
    print(expression_to_number("MY-MISERABLE-JOB"))
    print(expression_to_number("The quick brown fox jumps over the lazy dog"))
