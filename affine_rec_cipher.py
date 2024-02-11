from utilities import *
from affine_cipher import *
from modular_inverse import modular_inverse, extended_euclidean_algorithm
from utilities import f

a1, b1, a2, b2, alphabet, ssc_key = f()


def affine_rec_cipher_encrypt(text_arc):
    global a1, b1, a2, b2
    encrypted_text_arc = ""
    for index_arc, char_arc in enumerate(text_arc):
        if index_arc == 0:
            encrypted_text_arc += affine_cipher_encrypt(char_arc, a1, b1)
        elif index_arc == 1:
            encrypted_text_arc += affine_cipher_encrypt(char_arc, a2, b2)
        else:
            a1 = (a2 * a1) % 26
            b1 = (b2 + b1) % 26
            encrypted_text_arc += affine_cipher_encrypt(char_arc, a1, b1)
            a1, a2 = a2, a1
            b1, b2 = b2, b1
    return encrypted_text_arc



