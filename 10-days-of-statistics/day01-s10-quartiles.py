i_wont_use_you = int(input())
numbers = list(map(int, input().split(" ")))
numbers.sort()

def get_average(arr):
    return sum(arr) / len(arr)

def get_median(arr):
    n = len(arr)
    if n % 2 == 0:
        return get_average([arr[n//2], arr[(n//2)-1]])
    else:
        return arr[n//2]

first_half = numbers[:len(numbers)//2]
second_half = numbers[-(len(numbers)//2):]

q1 = get_median(first_half)
q2 = get_median(numbers)
q3 = get_median(second_half)

print("%d" % q1)
print("%d" % q2)
print("%d" % q3)
