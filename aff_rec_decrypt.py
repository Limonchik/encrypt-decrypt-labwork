from affine_cipher import *
from utilities import f

a1, b1, a2, b2, alphabet, ssc_key = f()


def affine_rec_cipher_decrypt(text_arc):
    global a1, b1, a2, b2
    decrypted_text_arc = ""
    for index_arc, char_arc in enumerate(text_arc):
        if index_arc == 0:
            decrypted_text_arc += affine_cipher_decrypt(char_arc, a1, b1)
        elif index_arc == 1:
            decrypted_text_arc += affine_cipher_decrypt(char_arc, a2, b2)
        else:
            a1 = (a2 * a1) % 26
            b1 = (b2 + b1) % 26
            decrypted_text_arc += affine_cipher_decrypt(char_arc, a1, b1)
            a1, a2 = a2, a1
            b1, b2 = b2, b1
    return decrypted_text_arc
