from collections import OrderedDict

od = OrderedDict()

for _ in range(int(input())):
    line = input().split(" ")
    product, price = ' '.join(line[:-1]), int(line[-1])
    if not product in od:
        od[product] = 0
    od[product] += price

for temp in od:
    print(temp, od[temp])