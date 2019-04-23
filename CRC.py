import sys
import utils

ENCODER = '-e'
DECODER = '-d'


class Encoder:
    def __init__(self, msg, polynomial):
        self.msg = msg
        self.polynomial = polynomial
        self.chars = utils.string_to_ascii_dict(msg)
        self.char_encoded = dict()

    def encode(self):
        for char, code in self.chars.items():
            #print(f'Encode {code}')
            self.char_encoded[char] = self.xor_operation(code)
            #print(f'Character {char} encoded to {result}\n')

        ans = ""
        for char in self.msg:
            ans += hex(int(self.chars[char], 2))[2:] + hex(int(self.char_encoded[char], 2))[2:]
            #print(f'{char} = {self.char_encoded[char]}\n')
        print(ans)



    def xor_operation(self, code):
        code = code.ljust(len(code)+len(self.polynomial)-1, "0")
        #print(f'Code transformed to {code}\n')
        x = code[0:len(self.polynomial)]
        y = self.polynomial if int(x[0]) != 0 else "0" * len(self.polynomial)
        previews = utils.xor_in_list(x, y)

        for i in range(len(code)-len(self.polynomial)):

            x = previews[1:] + code[i+len(self.polynomial)]
            y = self.polynomial if int(x[0]) != 0 else "0" * len(self.polynomial)

            previews = utils.xor_in_list(x, y)
        return previews[1:]


class Decoder:
    def __init__(self, msg, polynomial):
        self.msg = msg
        self.polynomial = polynomial

    def decode(self):
        pass


operation = sys.argv[1]
msg = sys.argv[2]
polynomial = sys.argv[3]


if operation == ENCODER:
    enc = Encoder(msg, polynomial)
    enc.encode()
elif operation == DECODER:
    dec = Decoder(msg, polynomial)
    dec.decode()
