def discard_all(parent_set, set_to_discard):
    for i in set_to_discard:
        parent_set.discard(i)
    return parent_set

n = int(input())
set_1 = set(int(x) for x in input().split(' '))
m = int(input())
set_2 = set(int(x) for x in input().split(' '))

inter = set_1.intersection(set_2)
result = discard_all(set_1, inter).union(discard_all(set_2, inter))

for x in sorted(result):
    print(x)