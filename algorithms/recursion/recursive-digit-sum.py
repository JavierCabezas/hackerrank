n, k = input().split(" ")
p = n

def initial_sum(s, k):
    return int(digit_sum(s)) * k

def digit_sum(s):
    return str(sum(map(int, list(s))))

initial_sum(p, int(k))
while len(p) > 1:
    p = digit_sum(p)

print(p)