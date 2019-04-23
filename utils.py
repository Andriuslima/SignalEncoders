from operator import xor


def string_to_ascii_dict(string):
    ans = {}
    for char in string:
        ans[char] = bin(ord(char))[2:].rjust(7, "0")
    return ans


def xor_in_list(x, y):
    ans = ""
    if len(x) != len(y):
        raise ValueError(f'Not the same length: {x} and {y}\n')
    for i in range(len(x)):
        ans += str(int(xor(int(x[i]), int(y[i]))))
    return ans
