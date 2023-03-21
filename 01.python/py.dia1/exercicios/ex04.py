NAMES = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def bigger_name(list):
    bigger = ""
    for name in list:
        if len(name) > len(bigger):
            bigger = name
    return bigger


print(bigger_name(NAMES))
