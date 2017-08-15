#Project Euler #5: Smallest multiple

#  n  | min   |  mult           |  pow
#  1  |  1    |  1              |  1
#  2  |  2    |  2              |  2ˆ1
#  3  |  6    |  3*2            |  3ˆ1 * 2ˆ1
#  4  |  12   |  3*2*2          |  3ˆ1 * 2ˆ2
#  5  |  60   |  5*3*2*2        |  5ˆ1 * 3ˆ1 * 2ˆ2
#  6  |  60   |  5*3*2*2        |  5ˆ1 * 3ˆ1 * 2ˆ2
#  7  |  420  |  7*5*3*2*2      |  7ˆ1 * 5ˆ1 * 3ˆ1 * 2ˆ2
#  8  |  840  |  7*5*3*2*2*2    |  7ˆ1 * 5ˆ1 * 3ˆ1 * 2ˆ3
#  9  |  2520 |  7*5*3*3*2*2*2  |  7ˆ1 * 5ˆ1 * 3ˆ2 * 2ˆ3
#  10 |  2520 |  7*5*3*3*2*2*2  |  7ˆ1 * 5ˆ1 * 3ˆ2 * 2ˆ3

dict = {1:1}
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

number_of_testcases = int(input())
numbers_to_check = [int(input()) for _ in range(number_of_testcases)]

def get_value(n):
    if dict[n-1] %n == 0:
        dict[n] = dict[n-1]
        return dict[n]
    else:
        for prime in primes:
            if (dict[n-1] * prime ) % n == 0:
                dict[n] = dict[n-1] * prime
                return dict[n]

for n in numbers_to_check:
    for i in range(1, n+1):
        if i not in dict:
            get_value(i)
    print(dict[n])

