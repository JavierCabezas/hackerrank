from collections import Counter

c = Counter(input().strip())
for element in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:3]: #-x[1] sorts by quantity (desc) and then x[0] sorts by letter (asc)
    print(element[0], element[1])