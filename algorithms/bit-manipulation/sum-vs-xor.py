def number_of_zeroes(number):
    return bin(number).count("0") - 1

n = int(input())
print( 2 ** number_of_zeroes(n) if n != 0 else 1)