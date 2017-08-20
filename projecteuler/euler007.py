#Project Euler #7: 10001st prime

import math

number_of_testcases = int(input())
numbers_to_check = [int(input()) for _ in range(number_of_testcases)]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#This function does not check pair numbers (because the step goes +2 insted of +1)
def is_prime(n):
    sup_range = int(math.floor(math.sqrt(n))) + 1
    for i in range(3, sup_range):
        if n % i == 0:
            return False

    return True

def get_next_prime():
    last_prime = primes[-1]
    to_check = last_prime + 2
    was_prime_found = False
    while not was_prime_found:
        if is_prime(to_check):
            was_prime_found = True
            primes.append(to_check)
        else:
            to_check += 2

for n in numbers_to_check:
    while len(primes) < n:
        get_next_prime()
    print(primes[n-1])
