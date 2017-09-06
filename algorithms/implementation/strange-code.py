t = int(input())

counter = 0
i = 0
last_number = 0
if t == 1:
    print(3)
else:
    while True:
        counter += 3 * 2 ** i
        if t > counter:
            i += 1
            last_number = counter + 1
        else:
            break

    print(last_number + 2 - (t-last_number))