#For some reason on hackerrank the name of this challenge is angry-children. This is Max Min.
import math

number_of_integers = int(input())
range_size = int(input())
integers = [int(input()) for _ in range(number_of_integers)]

integers.sort()
selected_numbers = []
min_dif = math.inf
for i in range(number_of_integers-range_size+1):
    if integers[i+range_size-1] - integers[i] < min_dif:
        min_dif = integers[i+range_size-1] - integers[i]
        selected_numbers = [integers[n] for n in range(i, i+range_size)]

print(max(selected_numbers) - min(selected_numbers))