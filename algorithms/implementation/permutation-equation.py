p = [-1]  # p[0] won't be used
i_dont_need_you = input()
for number in input().split(" "):
    p.append(int(number))  # p[1], p[2], ...

for i in range(1, len(p)):
    idx = p.index(i)
    inverse = p.index(idx)
