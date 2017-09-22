def number_needed(a, b):
    checker = {}
    for char in a:
        if not char in checker:
            checker[char] = 0
        checker[char] += 1

    for char in b:
        if not char in checker:
            checker[char] = 0
        checker[char] -= 1

    total = 0
    for key in checker:
        total += abs(checker[key])
    return(total)

a = input().strip()
b = input().strip()

print(number_needed(a, b))