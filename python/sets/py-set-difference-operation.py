number_of_elements_a = int(input())
a = set(list(int(x) for x in input().split(" ")))
number_of_elements_b = int(input())
b = set(list(int(x) for x in input().split(" ")))

print(len(a.difference(b)))