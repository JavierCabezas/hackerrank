#Project Euler #1: Multiples of 3 and 5
t = int(input().strip())

def ari_sum(num):
    return num*(num+1)//2

for a0 in range(t):
    n = int(input().strip())
    m3 = (n-1)//3
    m5 = (n-1)//5
    m15 = (n-1)//15
    print(3*ari_sum(m3) + 5*ari_sum(m5) - 15*ari_sum(m15))