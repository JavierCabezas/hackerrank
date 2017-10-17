money = int(input().split(" ")[0])
keyboards = sorted(list(int(x) for x in input().split(" ")))
mouses = sorted(list(int(x) for x in input().split(" ")))

spent = -1
for k in keyboards:
    for m in mouses:
        if m + k > money:
            break
        spent = max(spent, m + k)

print(spent)