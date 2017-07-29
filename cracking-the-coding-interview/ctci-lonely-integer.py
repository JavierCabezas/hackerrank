def lonely_integer(a):
    if len(a) < 1:
        return False

    out = a[0]
    for i in range(1, len(a)):
        out = out ^ a[i]
    return out


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

