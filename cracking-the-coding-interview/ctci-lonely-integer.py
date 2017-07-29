def lonely_integer(a):
    if len(a) < 1:
        return False
    if len(a) < 2:
        return a[0]

    a.sort()
    last_number = None
    for i in range(len(a)):
        if last_number is not None:
            if last_number != a[i]:
                return last_number # We found the lonely integer
            else:
                last_number = None #Ok, they are equal. Reset the array
        else:
            last_number = a[i]

    return last_number #If we didn't return anything so far then the last_number stored is the lonely integer.

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

