#Project Euler #10: Summation of primes
number_of_testcases = int(input())
numbers_to_check = [int(input()) for _ in range(number_of_testcases)]

def get_closest_prime(n):
    while not bool_primes[n]:
        n = n-1
    return n

def fill_prime_and_prime_sum(bool_primes):
    sum = 0
    primes = []
    prime_sum = []

    for index, is_prime in enumerate(bool_primes):
        if is_prime:
            primes.append(index)
            sum += index
            prime_sum.append(sum)

    return primes, prime_sum


def fill_prime_array_up_to(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if (primes[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1

    primes[0] = False
    primes[1] = False
    return primes

bool_primes = fill_prime_array_up_to(max(numbers_to_check))
primes, prime_sum = fill_prime_and_prime_sum(bool_primes)

for n in numbers_to_check:
    n = get_closest_prime(n) #Get the closest prime number (rounding down in case is needed)
    location = primes.index(n)
    print(prime_sum[location])