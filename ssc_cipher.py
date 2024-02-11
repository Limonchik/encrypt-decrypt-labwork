from affine_cipher import alphabet, ssc_key
from utilities import *


def ssc_encrypt(text):

    cipher_dict = {alphabet[i]: ssc_key[i] for i in range(len(alphabet))}

    encrypted_text = ""
    for char in text:
        if char.upper() in cipher_dict:
            if char.islower():
                encrypted_text += cipher_dict[char.upper()].lower()
            else:
                encrypted_text += cipher_dict[char.upper()]
        else:
            encrypted_text += char

    return encrypted_text


def ssc_decrypt(text):

    decipher_dict = {ssc_key[i]: alphabet[i] for i in range(len(alphabet))}

    decrypted_text = ""
    for char in text:
        if char.upper() in decipher_dict:
            if char.islower():
                decrypted_text += decipher_dict[char.upper()].lower()
            else:
                decrypted_text += decipher_dict[char.upper()]
        else:
            decrypted_text += char

    return decrypted_text
