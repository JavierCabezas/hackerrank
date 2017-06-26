def partition(ar):
    pivot = ar[0]
    equal, right, left = [], [], []

    for i in ar:
        if i == pivot:
            equal.append(i)
        elif i > pivot:
            right.append(i)
        else :
            left.append(i)

    return [equal, left, right ]

def printArr(arr):
    for temp in arr:
        print(temp, end=' ')

m = input()
ar = [int(i) for i in input().strip().split()]
equal, left, right = partition(ar)
printArr(left)
printArr(equal)
printArr(right)