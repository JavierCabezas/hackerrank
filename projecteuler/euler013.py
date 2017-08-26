number_of_numbers = int(input())
numbers = [int(input()) for _ in range(number_of_numbers)]

sum_of_numbers = str(sum(numbers))
print(sum_of_numbers[0:10])