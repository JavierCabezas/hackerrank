from collections import defaultdict
d = defaultdict(list)

n_group_a, n_group_b = map(int, input().split(" "))
for i in range(n_group_a):
    d[input()].append(i+1)

words_in_b = [input() for _ in range(n_group_b)]
for word in words_in_b:
    if word in d:
        print(*d[word], sep=' ')
    else:
        print(-1)