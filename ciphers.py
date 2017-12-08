# -*- coding: utf-8 -*-
from random import choice

from utils import char_to_binary_string, binary_string_to_char


class StreamCipher:
    """
    the implementation of StreamCipher
    """
    @staticmethod
    def test():
        cipher = StreamCipher()
        cipher_text, keys = cipher.encrypt("hello, world")
        print(cipher_text, "cipher text")
        print(keys, "kes")
        clear_text = cipher.decrypt(cipher_text, keys)
        print(clear_text, "<------- clear text")

    @staticmethod
    def generate_key(length):
        res = []
        for i in range(length):
            res.append(choice(['0', '1']))
        return ''.join(res)

    @staticmethod
    def mod2calculus(x, y):
        res = (int(x) + int(y)) % 2
        return str(res)

    @staticmethod
    def encrypt_char(binary_string, key):
        res = []
        for x, y in zip(binary_string, key):
            res.append(StreamCipher.mod2calculus(x, y))
        return ''.join(res)

    @staticmethod
    def decrypt_char(binary_string, key):
        res = []
        for x, y in zip(binary_string, key):
            res.append(StreamCipher.mod2calculus(x, y))
        return ''.join(res)

    @staticmethod
    def encrypt(clear_text):
        res = []
        keys = []
        for char in clear_text:
            a = char_to_binary_string(char)
            key = StreamCipher.generate_key(len(a))
            cipher_text = StreamCipher.encrypt_char(a, key)
            keys.append(key)
            res.append(cipher_text)
        return res, keys

    @staticmethod
    def decrypt(cipher_text, key):
        res = []
        for char, char_key in zip(cipher_text, key):
            binary = StreamCipher.decrypt_char(char, char_key)
            temp = binary_string_to_char(binary)
            res.append(temp)
        return ''.join(res)


if __name__ == '__main__':
    StreamCipher.test()