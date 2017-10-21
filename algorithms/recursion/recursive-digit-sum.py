n, k = input().split(" ")
r = int(n) % 9 * int(k) % 9
print(r if r > 0 else 9)