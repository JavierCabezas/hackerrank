number_of_testcases = int(input())
numbers_to_check = [int(input()) for _ in range(number_of_testcases)]
fibo = [0]

def calculate_fibonacci(max_number):
    current = 0
    previous = 1
    i = 1
    while fibo[-1] < max_number:
        temp = current
        current = current + previous
        previous = temp
        fibo.append(current)
        i += 1


calculate_fibonacci(max(numbers_to_check))

for n in numbers_to_check:
    if n in fibo:
        print('IsFibo')
    else:
        print('IsNotFibo')