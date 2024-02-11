from affine_rec_cipher import affine_rec_cipher_encrypt
from aff_rec_decrypt import affine_rec_cipher_decrypt
from ssc_cipher import *
from affine_cipher import *

print('Если хотите зашифровать, введите "encrypt", для дешифрования "decrypt":')
while True:
    type = input()
    if type == "encrypt" or type == "decrypt":
        break

print('Введите слово:')
word = input()

if type == "encrypt":
    print('Выберите тип шифрования')

    print({
        'Шифр простой замены':
            'ssc_encrypt',
        'Афинный шифр':
            'affine_cipher_encrypt',
        'Афинный рекурретный шифр':
            'affine_rec_cipher_encrypt'
    })

    while True:
        type = input()
        if type == "ssc_encrypt" or type == "affine_cipher_encryp" or type == 'affine_rec_cipher_encrypt':
            break

    if type == "ssc_encrypt":
        print(ssc_encrypt(word))
    elif type == "affine_cipher_encrypt":
        print(affine_cipher_encrypt(word))
    else:
        print(affine_rec_cipher_encrypt(word))


else:
    print('Выберите тип дешифрования')

    print({
        'Шифр простой замены':
            'ssc_decrypt',
        'Афинный шифр':
            'affine_cipher_decrypt',
        'Афинный рекурретный шифр':
            'affine_rec_cipher_decrypt'
    })

    while True:
        type = input()
        if type == "ssc_decrypt" or type == "affine_cipher_decrypt" or type == 'affine_rec_cipher_decrypt':
            break

    if type == "ssc_decrypt":
        print(ssc_decrypt(word))
    elif type == "affine_cipher_decrypt":
        print(affine_cipher_decrypt(word))
    else:
        print(affine_rec_cipher_decrypt(word))
