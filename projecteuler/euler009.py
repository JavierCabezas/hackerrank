from functools import reduce

number_of_testcases = int(input())
numbers_to_check = [int(input()) for _ in range(number_of_testcases)]

for n in numbers_to_check:
    pairs = [[a, b, c] for a in range(1, n-2) for b in range(1, n-2) for c in range(1, n-2) if a**2 + b**2 == c**2]
    if len(pairs) == 0:
        print(-1)
    else:
        print(reduce(lambda x, y: x*y, pairs[-1]))