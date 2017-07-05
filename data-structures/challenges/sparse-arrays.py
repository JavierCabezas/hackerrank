dict = {}
N = int(input())
for _ in range(N):
    temp = str(input())
    if temp in dict:
        dict[temp] += 1
    else:
        dict[temp] = 1

N = int(input())
for _ in range(N):
    temp = str(input())
    if temp in dict:
        print(dict[temp])
    else:
        print(0)