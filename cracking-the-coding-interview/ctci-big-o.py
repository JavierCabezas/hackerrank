import math

def check_prime(n):
    is_prime = True
    if(n <= 1):
        is_prime = False
    elif n%2 == 0 and n != 2 or n%3 == 0:
        is_prime = False
    elif(n%5 == 0 and n != 5):
        is_prime = False
    else:
        i = 5
        while math.sqrt(n) >= i:
            if n%i == 0:
                is_prime = False
                break
            i+=2

    return is_prime

n = int(input())
to_be_checked = [ int(input()) for _ in range(0, n)]

for candidate in to_be_checked:
    if(check_prime(candidate)):
        print("Prime")
    else:
        print("Not prime")