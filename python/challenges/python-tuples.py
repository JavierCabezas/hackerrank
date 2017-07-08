n = int(input())
integer_list = list(map(int, input().split()))

t = tuple(integer_list)
print(hash(t))