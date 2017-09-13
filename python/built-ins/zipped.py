n, lines = map(int, input().split())
ave = []
for _ in range(lines):
    ave.append(list(map(float, input().split())))

for ave_list in list(zip(*ave)):
    print("{0:.2f}".format(sum(ave_list) / len(ave_list)))