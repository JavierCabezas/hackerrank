numbers = input().split(" ")
t1, t2, n = int(numbers[0]), int(numbers[1]), int(numbers[2])

memory_fibo = {}
memory_fibo[1] = t1
memory_fibo[2] = t2

def get_fibo(n):
    if n in memory_fibo:
        return memory_fibo[n]
    else:
        memory_fibo[n] = memory_fibo[n-2] + memory_fibo[n-1] ** 2
        return memory_fibo[n]

for i in range(3, n+2):
    get_fibo(i-2) + get_fibo(i-1) ** 2

print(memory_fibo[n])