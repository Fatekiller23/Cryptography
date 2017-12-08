# -*- coding: utf-8 -*-
"""
this script implment some ciphers
ceaser cipher,  affine ceaser, stream cipher,extra.
"""

from random import choice

raw = 'abcdefghijklmnopqrstuvwxyz'


class StreamCipher:
    def to_binary(self, text):
        res = []
        for each in text:
            bits = bin(ord(each))[2:]
            res.append(bits)
        return res

    def to_word(self, binary_list):
        res = []
        for each in binary_list:
            letter = chr(int(each, 2))

            res.append(letter)
        result = ''.join(res)
        return result

    def encrypt_one(self, plain_text):
        keys = []
        encrypt_text = []
        for each in plain_text:
            one_bit_key = choice([0, 1])
            one_bit_text = int(each)
            res = (one_bit_key + one_bit_text) % 2

            encrypt_text.append(str(res))
            keys.append(str(one_bit_key))

        keys = ''.join(keys)
        encrypt_text = ''.join(encrypt_text)

        return keys, encrypt_text

    def decrypt_one(self, text, stream_keys):
        clear_text = []

        for i in range(len(text)):
            each_text = int(text[i])
            each_key = int(stream_keys[i])
            res = (each_text + each_key) % 2
            clear_text.append(str(res))
        return ''.join(clear_text)

    def encrypt(self, text):
        temp = self.to_binary(text)
        keys = []
        e_text = []
        for each_letter in temp:
            key, e_t = self.encrypt_one(each_letter)

            keys.append(key)
            e_text.append(e_t)

        return keys, e_text

    def decrypt(self, black, key_list):
        letters = []
        assert len(black) == len(key_list)
        for i in range(len(black)):
            one_letter = black[i]
            key = key_list[i]
            letter = self.decrypt_one(one_letter,key)
            letters.append(letter)
        clear_text = self.to_word(letters)
        return clear_text

if __name__ == '__main__':
    cipher = StreamCipher()
    clear = 'i\'m great'
    keys, text = cipher.encrypt(clear)
    print(keys, text)
    text = cipher.decrypt(text, keys)
    print(text)