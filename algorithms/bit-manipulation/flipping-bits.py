number_of_numbers = int(input())
numbers = [int(input()) for _ in range(number_of_numbers)]

for n in numbers:
    print(2 ** 32 - n - 1)