def average(array):
    return sum(array)/len(array)

n = int(input())
arr = set([int(x) for x in (input().split(' '))])
print(average(arr))