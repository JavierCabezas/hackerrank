#Project Euler #2: Even Fibonacci numbers

#  n  | fib(n)  | sum
#  3  |   2     |  2
#  6  |   8     |  10
#  9  |   34    |  44
#  12 |   144   |  188
#  15 |   610   |  798
#  18 |   2584  |  3382
#  21 |   10946 |  14328
#  24 |   46368 |  60696

results = {3: 2, 6:8} #First two even elements

def calculate_even_fibo(n):
    sum = 0
    multiple_3 = n-n%3
    for i in range(3,multiple_3+1,3):
        if not i in results:
            results[i] = 4 * results[i-3] + results[i-6]
        if results[i] > n:
            return sum
        else:
            sum += results[i]


number_of_test_cases = int(input())
numbers_to_fibo = [int(input()) for _ in range(number_of_test_cases)]
for n in numbers_to_fibo:
    print(calculate_even_fibo(n))