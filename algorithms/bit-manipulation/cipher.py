from operator import xor

n, k = map(int, input().split(" "))
b = [0] * n

s = list(map(int, input()))
b[0] = s[0]
b[-1] = s[-1]

for bit in range(1, min(k, n)):
    b[bit] = xor(s[bit-1], s[bit])

i = 0
for bit in range(k, n):
    b[bit] = xor(xor(s[bit-1], s[bit]), b[i])
    i += 1

for i in b:
    print(i, end='')