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

        out = quicksort(left) + [ pivot ] + quicksort(right)
        printArr(out)
        return out

def printArr(arr):
    if(len(arr) > 0):
        for temp in arr:
            print(temp, end=' ')
        print("")

m = input()
ar = [int(i) for i in input().strip().split()]
sorted_array = quicksort(ar)