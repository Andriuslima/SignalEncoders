import sys
from operator import xor

ENCODER = '-e'
DECODER = '-d'
DEBUG = False
ASCII_LEN = 7


def string_to_ascii_dict(string):
    ans = {}
    for char in string:
        ans[char] = bin(ord(char))[2:].rjust(ASCII_LEN, "0")
    return ans


def xor_in_string(x, y):
    ans = ""
    if len(x) != len(y):
        raise ValueError(f'Not the same length: {x} and {y}\n')
    for i in range(len(x)):
        ans += str(int(xor(int(x[i]), int(y[i]))))
    return ans


def xor_operation(code, poly):
    code = code.ljust(len(code)+len(poly)-1, "0")
    x = code[0:len(poly)]
    y = poly if int(x[0]) != 0 else "0" * len(poly)
    previews = xor_in_string(x, y)

    for i in range(len(code)-len(poly)):

        x = previews[1:] + code[i+len(poly)]
        y = poly if int(x[0]) != 0 else "0" * len(poly)

        previews = xor_in_string(x, y)
    return previews[1:]


class CRC:
    def __init__(self, message, poly):
        self.msg = message
        self.polynomial = poly
        self.chars = string_to_ascii_dict(msg)
        self.char_encoded = dict()

    def encode(self):
        for char, code in self.chars.items():
            self.char_encoded[char] = xor_operation(code, self.polynomial)

        ans = ""
        for char in self.msg:
            ans += hex(int(self.chars[char], 2))[2:] + hex(int(self.char_encoded[char], 2))[2:]
        print(ans, file=sys.stdout)

    def decode(self):
        ans = ""
        if len(self.msg) % 3:
            raise ValueError(f'Not the correct length: {self.msg}\n')
        for i in range(0, len(self.msg)-1, 3):
            char = bin(int(self.msg[i:i+2], 16))[2:]
            code = bin(int(self.msg[i+2], 16))[2:].zfill(4)

            result = xor_operation(char+code, self.polynomial)
            if DEBUG:
                print(f'char: {char} | poly: {code} | result: {result}')
            if int(result) == 0:
                ans += chr(int(char, 2))
            else:
                ans += chr(95)
        print(ans, file=sys.stdout)


operation = sys.argv[1]
msg = sys.argv[2]
polynomial = sys.argv[3]

crc = CRC(msg, polynomial)

if operation == ENCODER:
    crc.encode()

elif operation == DECODER:
    crc.decode()
