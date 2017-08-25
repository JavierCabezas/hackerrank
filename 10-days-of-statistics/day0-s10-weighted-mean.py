i_wont_use_you = int(input())
numbers = list(map(int, input().split(" ")))
weights = list(map(int, input().split(" ")))

numbers = [numbers[i] * weights[i] for i in range(len(numbers))]

weighted_average = sum(numbers) / sum(weights)
print("%.1f" % weighted_average)
