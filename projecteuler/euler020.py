number_of_testcases = int(input())
numbers_to_check = [ int(input()) for _ in range(number_of_testcases)]

factorials = {0:1, 1: 1}
factorial_sum  = {0:1, 1:1}

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def fill_factorial(n):
    for current in range(2, n+1):
        factorials[current] = current * factorials[current-1]
        factorial_sum[current] = sum_digits(factorials[current])


fill_factorial(max(numbers_to_check))
for n in numbers_to_check:
    print(factorial_sum[n])