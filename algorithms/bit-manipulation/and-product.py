from collections import namedtuple
Pair = namedtuple('Pair', 'a, b')

number_of_testcases = int(input())
cases = []
for _ in range(number_of_testcases):
    a, b = map(int, input().split(" "))
    cases.append(Pair(a=a, b=b))


def long_and(numbers):
    out = numbers.a & numbers.b
    i = 0
    while (numbers.a + 2 ** i) < numbers.b:
        out &= numbers.a + 2 ** i
        i+=1
    return out

for case in cases:
    print(long_and(case))