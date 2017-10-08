from math import log2, ceil
number_of_testcases = int(input())
numbers_to_check = list(int(input()) for _ in range(number_of_testcases))


def number_of_binary_digits(number):
    return ceil(log2(number+1))


for n in numbers_to_check:
    print( (2 ** number_of_binary_digits(n)) - (n + 1) )