from math import sqrt

i_wont_use_you = int(input())
x = list(map(int, input().split(" ")))

def get_average(arr):
    return sum(arr) / len(arr)

def get_std(arr):
    x_bar = get_average(arr)
    top = sum(list(map(lambda x: (x-x_bar) ** 2, arr)))
    return sqrt(top/len(arr))

std = get_std(x)
print("%.1f" %std)