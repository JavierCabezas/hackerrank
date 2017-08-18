#Project Euler #8: Largest product in a series

from functools import reduce

number_of_testcases = int(input())
max_mults = []
for _ in range(number_of_testcases):
    digits = int(input().split(" ")[1])
    number = [int(x) for x in input()]

    max_mult = 0
    for i in range(len(number) - digits):
        m = reduce(lambda x, y: x*y, number[i:i+digits])
        if m > max_mult:
            max_mult = m

    max_mults.append(max_mult)

for m in max_mults:
    print(m)