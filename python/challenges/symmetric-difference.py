n = int(input())
set_1 = set(int(x) for x in input().split(' '))
m = int(input())
set_2 = set(int(x) for x in input().split(' '))

inter = set_1.intersection(set_2)
result = set_1.difference(inter).union(set_2.difference(inter))

for x in sorted(result):
    print(x)