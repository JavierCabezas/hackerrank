from itertools import groupby

for k, g in groupby(input()):
    number = int(k)
    number_of_times = len(list(g))
    print("({}, {})".format(number_of_times, number), end=" ")