n = int(input())
integer_list = [i for i in input().split(' ')]
sorted_uniques = sorted({int(i) for i in integer_list})
if len(sorted_uniques) > 1:
    print(sorted_uniques[-2])