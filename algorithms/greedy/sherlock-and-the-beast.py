#n = F+t where F is the number of 5s and T is the number of 3s
def find_x_y_combinations(n):
    for i in range(n+1):
        f = n-i
        t = i
        if f%3 == 0 and t%5 == 0:
            return (f, t)
        i+=1
    raise Exception('not_found')


t = int(input().strip())
values = [int(input()) for _ in range(t)]

for n in values:
    try:
        f, t = find_x_y_combinations(n)
        number = ''
        for _ in range(f):
            number += str(5)
        for _ in range(t):
            number += str(3)
        print(number)
    except Exception:
        print(-1)




