big_string, small_string = input(), input()
count = 0
for i in range(len(big_string) - len(small_string) +1):
    if big_string[i:(i+len(small_string))] == small_string:
        count += 1

print(count)