number_of_items = int(input())
numbers = [int(x) for x in input().split(" ")]
numbers.sort()

print(numbers[number_of_items//2])