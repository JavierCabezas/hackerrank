a = input().strip()
b = input().strip()

def fill_dict():
    temp = {}
    for code in range(ord('a'), ord('z') + 1):
        temp[chr(code)] = 0

    for char in a:
        temp[char] += 1

    return temp

def check_dict(dict):
    for char in b:
        dict[char] -= 1

    return dict

def count_chars(dict):
    sum = 0
    for i in dict:
        sum += abs(dict[i])
    return sum

final_dict = check_dict(fill_dict())
print(count_chars(final_dict))