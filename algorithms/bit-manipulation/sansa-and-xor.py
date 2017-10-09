from operator import xor

number_of_testcases = int(input())
arrs_to_check = []
for _ in range(number_of_testcases):
    i_dont_need_you = input()
    arrs_to_check.append(list(map(int, input().split(" "))))


def odd_xor_sum(elements):
    out = 0
    for odd_index in range(0, len(elements), 2):
        out = xor(out, elements[odd_index])
    return out


for arr in arrs_to_check:
    if len(arr) < 2:
        print(0)
    elif len(arr) == 2:
        print(xor(*arr))
    else:
        if len(arr) % 2 == 0:
            print(0)
        else:
            print(odd_xor_sum(arr))