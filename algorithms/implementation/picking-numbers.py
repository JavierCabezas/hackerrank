n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

a.sort()
group_number = []
max = 0
for i in a:
    if len(group_number) > 0:
        if (i - group_number[0]) > 1:
            group_number.clear() #Difference is greater than 1: reset the array
    group_number.append(i)
    if len(group_number) > max:
        max = len(group_number)
print(max)