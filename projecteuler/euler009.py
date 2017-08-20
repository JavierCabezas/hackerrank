number_of_testcases = int(input())
numbers_to_check = [int(input()) for _ in range(number_of_testcases)]

#From a+b+c = n
#And a2 + b2 = c2
#We can get b = (n2 - 2an) / (2n-2a)
#n is known (in array numbers_to_check), so we must loop just for values of "a".

def get_b(a, n):
    return (n**2 - 2*a*n) / (2*(n-a))

for n in numbers_to_check:
    max_b = 0
    max_a = 0
    for a in range(1, n-1):
        b = get_b(a, n)
        if b.is_integer() and b*a > max_b*max_a:
            max_b = b
            max_a = a
    if max_b == 0:
        print(-1)
    else:
        print (int(max_a*max_b*(n-max_b-max_a)))