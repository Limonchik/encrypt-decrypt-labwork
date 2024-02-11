from modular_inverse import extended_euclidean_algorithm, modular_inverse
from utilities import *
a1, b1, a2, b2, alphabet, ssc_key = f()

def affine_cipher_encrypt(text, a=a1, b=b1):
    encrypted_text = ""
    for char in text:
        if char.upper() in alphabet:
            if char.isupper():
                char_index = alphabet.index(char)
                encrypted_index = (a * char_index + b) % len(alphabet)
                encrypted_char = alphabet[encrypted_index]
                encrypted_text += encrypted_char
            else:
                char_index = alphabet.index(char.upper())
                encrypted_index = (a * char_index + b) % len(alphabet)
                encrypted_char = alphabet[encrypted_index].lower()
                encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def affine_cipher_decrypt(text, a=a1, b=b1):
    decrypted_text = ""
    a_inverse = modular_inverse(a, len(alphabet))
    for char in text:
        if char.upper() in alphabet:
            if char.isupper():
                char_index = alphabet.index(char)
                decrypted_index = (
                    a_inverse * (char_index - b)) % len(alphabet)
                decrypted_char = alphabet[decrypted_index]
                decrypted_text += decrypted_char
            else:
                char_index = alphabet.index(char.upper())
                decrypted_index = (
                    a_inverse * (char_index - b)) % len(alphabet)
                decrypted_char = alphabet[decrypted_index].lower()
                decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
