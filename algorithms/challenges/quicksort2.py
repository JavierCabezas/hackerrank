def quicksort(ar):
    leng = len(ar)

    if(leng == 0):
        return []
    elif leng == 1: #We assume thats it's already sorted
        return [ar[0]]
    else:
        pivot = ar[0]
        right, left = [], [] #We assume we don't get equals
        ar.pop(0) #Delete the pivot from the list

        for i in ar:
            if i > pivot:
                right.append(i)
            else:
                left.append(i)

        return quicksort(left) + [ pivot ] + quicksort(right)

def printArr(arr):
    for temp in arr:
       print(temp, end=' ')

#m = input()
#ar = [int(i) for i in input().strip().split()]
ar = [30, 22, 8 ,21, 2, 6, 26, 25, 27, 3, 16, 9, 20, 23, 12, 4, 24, 5, 29, 17, 15, 18, 28, 10, 19, 7, 1, 11, 14, 13]
sorted_array = quicksort(ar)
print(sorted_array)