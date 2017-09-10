i_dont_need_you = input()
pool = list(map(int, input().split(" ")))
a = set(map(int, input().split(" ")))
b = set(map(int, input().split(" ")))

total = 0
for n in pool:
    if n in a:
        total += 1
    if n in b:
        total -= 1
print(total)