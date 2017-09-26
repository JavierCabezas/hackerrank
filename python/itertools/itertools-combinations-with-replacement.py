from itertools import combinations_with_replacement

word, how_long = input().split()

for c in combinations_with_replacement(sorted(word), int(how_long)):
    print(*c, sep='')