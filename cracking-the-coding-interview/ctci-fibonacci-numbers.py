values = {}
def fibonacci(n):
    if n in values:
        return values[n]
    else:
        if n > 1:
            values[n] = fibonacci(n-1) + fibonacci(n-2)
            return values[n]
        else:
            return n

n = int(input())
print(fibonacci(n))
