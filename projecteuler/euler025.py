#Project Euler #25: N-digit Fibonacci number
from math import sqrt
import decimal

min_fibo_for_digits = {}
fibo = {}

def fibonacci(digits):
    current = 0
    previous = 1
    i = 1
    should_continue = True
    while should_continue:
        temp = current
        current = current + previous
        previous = temp
        fibo[i] = current
        should_continue = get_digits_fibo(i) < digits
        i += 1

def get_digits_fibo(n):
    return len(str(fibo[n]))

current_fibo_number = 1
def get_next_fibo():
    global current_fibo_number

    should_continue_loop = True
    while should_continue_loop:
        digits = get_digits_fibo(current_fibo_number)
        if digits not in min_fibo_for_digits:
            min_fibo_for_digits[digits] = current_fibo_number
            should_continue_loop = False
        current_fibo_number += 1

number_of_testcases = int(input())
numbers_to_check = [int(input()) for _ in range(number_of_testcases)]

fibonacci(max(numbers_to_check))

for n in numbers_to_check:
    while not n in min_fibo_for_digits:
        get_next_fibo()
    print(min_fibo_for_digits[n])
