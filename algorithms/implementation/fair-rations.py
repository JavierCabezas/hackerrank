i_dont_need_you = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

if sum(B) % 2 == 1:
    print("NO")
else:
    total_movements = 0
    for index, element in enumerate(B):
        if element%2 == 1:
            total_movements += 2
            B[index+1] += 1
    print(total_movements)