from math import sqrt, ceil

a = int(input())
b = int(input())

def to_binary_list(n):
    starting_number = ceil(sqrt(n))
    out = [0] * starting_number
    for i in range(starting_number, -1, -1):
        if n - 2 ** i >= 0:
            out[i] = 1
            n -= 2 ** i
    return out

def fill_with_zeroes(little, big):
    while len(big) > len(little):
        little =  little + [0]
    return little

def get_first_dif(a, b):
    for i in range(len(b) - 1, -1, -1):
        if b[i] != a[i]:
            return i + 1
    return 0

a = to_binary_list(a)
b = to_binary_list(b)
a = fill_with_zeroes(a, b)
print(2 ** get_first_dif(a, b) -1)
