import sys
from math import log, ceil
from operator import xor

ENCODER = '-e'
DECODER = '-d'
DEBUG = False


def string_to_ascii_dict(string):
    ans = {}
    for char in string:
        ans[char] = bin(ord(char))[2:].rjust(7, "0")
    return ans

def xor_in_list(list):
    ans = ""
    for index in range(len(list[0])):
        xor_result = 0
        for number in list:
            xor_result = xor(int(number[index]), xor_result)
        ans += str(xor_result)
    return ans

def positions_with_one(l):
    result = list()
    for i in range(len(l)):
        if l[i] == '1':
            result.append(len(l)-i)
    return result

def insert_dash(list):
    index = 1
    while index <= len(list):
        list.insert(len(list)-index+1, '-')
        index *= 2
    return list


class Hamming:
    def __init__(self, msg):
        self.msg = msg
        self.chars = string_to_ascii_dict(self.msg)
        self.hamming_code = dict()

    def encode(self):
        for char, code in self.chars.items():
            print("="*20)
            print(f'original code => {code}')
            bits = ceil(log(len(code), 2))+1
            code_list = insert_dash(list(code))
            print(f'{code} => {code_list}')
            positions = positions_with_one(code_list)
            print(f'{code_list} ==with one=> {positions}')

            aux = list()
            result = ""
            for i in positions:
                aux.append(bin(i)[2:].zfill(bits))
            print(f'positions with one in binary ====> {aux}')
            xor_result = xor_in_list(aux)
            print(f'Xor result = {xor_result}')
            xor_result = list(xor_result)
            for index in range(len(code_list)):
                if code_list[index] == '-':
                    code_list[index] = xor_result.pop(0)
                result += code_list[index]

            self.hamming_code[char] = hex(int(result, 2))[2:]

            print(f'{char}: {code_list}')
            print(f'{char}: {self.hamming_code[char]}')

            print("="*20)
        result = ""
        for char in self.msg:
            result += self.hamming_code[char]
        print(result, file=sys.stdout)
            
    def decode(self):
        pass


operation = sys.argv[1]
msg = sys.argv[2]

hamming = Hamming(msg)

if operation == ENCODER:
    hamming.encode()

elif operation == DECODER:
    hamming.decode()
