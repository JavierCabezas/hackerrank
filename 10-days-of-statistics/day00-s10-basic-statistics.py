useless = int(input())
numbers = list(map(int, input().split(" ")))
numbers.sort()

def get_average(arr):
    return sum(arr) / len(arr)

def get_mean(arr):
    n = len(arr)
    if n % 2 == 0:
        return get_average([arr[n//2], arr[(n//2)-1]])
    else:
        return arr[n//2]

def get_mode(arr):
    current = { 'number': None, 'times': 0 }
    mode = { 'number': None, 'times': 0 }
    for n in arr:
        if n != current['number']:
            current['number'] = n
            current['times'] = 0
        current['times'] += 1
        if current['times'] > mode['times']:
            mode['number'] = current['number']
            mode['times'] = current['times']

    return int(mode['number'])


average = get_average(numbers)
mean = get_mean(numbers)
mode = get_mode(numbers)


print("%.1f" % average)
print("%.1f" % mean)
print(mode)
