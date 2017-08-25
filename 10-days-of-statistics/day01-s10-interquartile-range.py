i_wont_use_you = int(input())
x = list(map(int, input().split(" ")))
f = list(map(int, input().split(" ")))

def get_average(arr):
    return sum(arr) / len(arr)

def get_mean(arr):
    n = len(arr)
    if n % 2 == 0:
        return get_average([arr[n//2], arr[(n//2)-1]])
    else:
        return arr[n//2]

result = []
for i in range(len(x)):
    result += [x[i]] * f[i]
result.sort()

first_half = result[:len(result)//2]
second_half = result[-(len(result)//2):]

q1 = get_mean(first_half)
q3 = get_mean(second_half)

iqr = q3 - q1
print("%.1f" % iqr)
