def is_triangle(a, b, c):
    if a == b == c:
        return "Triângulo Equilátero: três lados iguais"
    elif a + b > c and a + c > b and c + b > a:
        if a == b or a == c or b == c:
            return "Triângulo Isósceles: quaisquer dois lados iguais"
        elif a != b != c:
            return "Triângulo Escaleno: três lados diferentes"
    else:
        return "Não é triangulo"


print(is_triangle(12, 10, 11))
