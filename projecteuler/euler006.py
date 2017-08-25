number_of_testcases = int(input())
numbers = [int(input()) for _ in range(number_of_testcases)]

def sum_of_squares(n):
    return n*(n+1)*(2*n+1)/6

def square_of_sum(n):
    return (n*(n+1)/2) ** 2

for n in numbers:
    result = abs(square_of_sum(n) - sum_of_squares(n))
    print("%d" % result)