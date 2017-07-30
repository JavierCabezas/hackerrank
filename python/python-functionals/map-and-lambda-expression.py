cube = lambda x: pow(x, 3)

dict_fibo = {}
dict_fibo[1] = 0
dict_fibo[2] = 1

def calculate_fibo(n):
    if n in dict_fibo:
        return dict_fibo[n]
    else:
        dict_fibo[n] = calculate_fibo(n-1)+calculate_fibo(n-2)
        return dict_fibo[n]

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    for i in range(1, n+1):
        calculate_fibo(i)
    return dict_fibo.values()


n = int(input())
print(list(map(cube, fibonacci(n))))