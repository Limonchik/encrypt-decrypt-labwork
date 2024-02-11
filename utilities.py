from modular_inverse import extended_euclidean_algorithm


def f():
    a1 = None
    b1 = None
    a2 = None
    b2 = None
    alphabet = None
    ssc_key = None
    with open('keys.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith('key1'):
            key1 = tuple(map(int, line.split('=')[1].strip()[1:-1].split(',')))
            a1, b1 = key1
        elif line.startswith('key2'):
            key2 = tuple(map(int, line.split('=')[1].strip()[1:-1].split(',')))
            a2, b2 = key2
        elif line.startswith('alphabet'):
            alphabet = line.split('=')[1].strip()
        elif line.startswith('simple substitution cipher key'):
            ssc_key = line.split('=')[1].strip()

    if len(alphabet) != len(ssc_key):
        print('Alphabet and key are not the same length.')
        exit()

    key1_gcd = extended_euclidean_algorithm(a1, len(alphabet))
    key2_gcd = extended_euclidean_algorithm(a2, len(alphabet))

    if key1_gcd[0] != 1:
        print('Key 1: Alphabet length and multiply part of the key must have the GCD of 1.')
        exit()
    if key2_gcd[0] != 1:
        print('Key 2: Alphabet length and multiply part of the key must have the GCD of 1.')
        exit()

    return a1, b1, a2, b2, alphabet, ssc_key
