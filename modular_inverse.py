def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclidean_algorithm(b, a % b)
        return d, y, x - (a // b) * y


def modular_inverse(a, m):
    d, x, y = extended_euclidean_algorithm(a, m)
    if d != 1:
        raise ValueError("The modular inverse does not exist.")
    else:
        return x % m


def main():
    a = int(input("Введите число, для которого хотите найти обратное: "))
    m = int(input("Введите модуль: "))
    try:
        inverse = modular_inverse(a, m)
        print("Обратное число по модулю", m, "для", a, ":", inverse)
    except ValueError as e:
        print(e)