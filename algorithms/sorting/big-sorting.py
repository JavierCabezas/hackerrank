q = int(input())
numbers = [input() for _ in range(q)]
numbers.sort(key=lambda y: int(y))
for n in numbers:
    print(n)