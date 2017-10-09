number_of_testcases = int(input())


def passes_test(arr_a, arr_b, min_value):
    for i in range(len(arr_a)):
        if arr_a[i] + arr_b[i] < min_value:
            return False
    return True

for _ in range(number_of_testcases):
    k = int(input().split(" ")[1])
    a = sorted(list(map(int, input().split(" "))))
    b = sorted(list(map(int, input().split(" "))), reverse=True)
    print("YES" if passes_test(a, b, k) else "NO")

