number_of_testcases = int(input())
stones = [int(input()) for _ in range(number_of_testcases)]

for stone in stones:
    if stone % 7 in [0, 1]:
        print("Second")
    else:
        print("First")