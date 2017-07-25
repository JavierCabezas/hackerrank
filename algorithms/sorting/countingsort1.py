def count(ar):
    out = [0] * 100
    for i in ar:
        out[i] += 1

    return out

def printArr(arr):
    for temp in arr:
        print(temp, end=' ')

m = input()
ar = [int(i) for i in input().strip().split()]
printArr(count(ar))