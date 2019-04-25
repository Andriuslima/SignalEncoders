import sys
from math import log, ceil
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


def list_to_string(l):
    result = ""
    for element in l:
        result += str(element)
    return result


def xor_in_list(l):
    ans = ""
    for index in range(len(l[0])):
        xor_result = 0
        for number in l:
            xor_result = xor(int(number[index]), xor_result)
        ans += str(xor_result)
    return ans


def positions_with_one(l):
    result = list()
    for i in range(len(l)):
        if l[i] == '1':
            result.append(len(l)-i)
    return result


def insert_dash(l):
    result = l
    index = 1
    while index <= len(result):
        result.insert(len(result)-index+1, '-')
        index *= 2
    return result


def remove_bits(l):
    result = l
    if DEBUG:
        print(f'before: {result}')
    index = 1
    while index <= len(result):
        result[len(result) - index] = '-'
        index *= 2
    result = [ele for ele in result if ele not in '-']
    if DEBUG:
        print(f'after: {result}')
    return result


def translate_to_char(code):
    if DEBUG:
        print(f'Going to translate this code ==> {code}')
    result = ""
    aux = remove_bits(code)
    if DEBUG:
        print(f'after bits removed ==> {aux}')
    for i in aux:
        result += i
    return chr(int(result, 2))


class Hamming:
    def __init__(self, message):
        self.msg = message

    def encode(self):
        chars = string_to_ascii_dict(self.msg)
        hamming_code = dict()

        for char, code in chars.items():
            if DEBUG:
                print("="*20)
                print(f'original code => {code}')

            bits = ceil(log(len(code), 2))+1
            code_list = insert_dash(list(code))

            if DEBUG:
                print(f'{code} => {code_list}')

            positions = positions_with_one(code_list)

            if DEBUG:
                print(f'{code_list} ==with one=> {positions}')

            positions_in_binary = list()
            for i in positions:
                positions_in_binary.append(bin(i)[2:].zfill(bits))

            if DEBUG:
                print(f'positions with one in binary ====> {positions_in_binary}')

            xor_result = xor_in_list(positions_in_binary)

            if DEBUG:
                print(f'Xor result = {xor_result}')

            xor_result = list(xor_result)

            # Replace the '-' by the numbers in xor operation
            result = ""
            for index in range(len(code_list)):
                if code_list[index] == '-':
                    code_list[index] = xor_result.pop(0)
                result += code_list[index]

            hamming_code[char] = hex(int(result, 2))[2:]

            if DEBUG:
                print(f'{char}: {code_list}')
                print(f'{char}: {hamming_code[char]}')
                print("="*20)

        result = ""
        for char in self.msg:
            result += hamming_code[char]
        print(result, file=sys.stdout)
            
    def decode(self):
        result = ""
        char_index = 1
        for i in range(0, len(self.msg), 3):
            code = list(bin(int(self.msg[i:i+3], 16))[2:])

            if DEBUG:
                print("="*20)
                print(f'Code = {code}')

            positions = positions_with_one(code)
            positions_in_binary = list()
            for j in positions:
                positions_in_binary.append(bin(j)[2:].zfill(ceil(log(len(code), 2)) + 1))

            xor_result = xor_in_list(positions_in_binary)
            bit = int(xor_result, 2)

            if bit == 0:
                if DEBUG:
                    print('ok')
                result += translate_to_char(code)
            else:
                pos_error = len(code) - bit
                if DEBUG:
                    print(f'This is the code with error on bit {bit}/{pos_error}: {code}')
                code[pos_error] = str(int(not(bool(int(code[pos_error])))))
                if DEBUG:
                    print(f'Final code: {code}')
                correction = translate_to_char(code)
                result += correction
                print(f'ERROR on character {char_index} (bit {bit}) -> Correction: {correction}')
                if DEBUG:
                    print(f'xor result: {xor_result}')
            char_index += 1
            if DEBUG:
                print("=" * 20)

        print(result, file=sys.stdout)


operation = sys.argv[1]
msg = sys.argv[2]
hamming = Hamming(msg)

if operation == ENCODER:
    hamming.encode()
    sys.exit(0)
if operation == DECODER:
    hamming.decode()
    sys.exit(0)
