number_of_testcases = int(input())
arrays_to_check = []
for _ in range(number_of_testcases):
    i_dont_need_you = input()
    arrays_to_check.append(list(map(int, input().strip().split(' '))))

def check_array(arr):
    sum_array = sum(arr)
    left_sum = 0
    for current_element in arr:
        right_sum = sum_array - (current_element + left_sum)
        if left_sum == right_sum:
            return('YES')
        left_sum += current_element

    return('NO')


for a in arrays_to_check:
    print(check_array(a))