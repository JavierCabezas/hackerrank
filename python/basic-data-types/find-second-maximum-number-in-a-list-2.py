_ = input()
values = [int(x) for x in input().split()]
values = list(set(values))
values.sort(reverse=True)
print(values[1])