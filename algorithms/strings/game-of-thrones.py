letters = {}

string_to_check = input()
for char in string_to_check:
    if char in letters:
        del letters[char]
    else:
        letters[char] = 1

if len(letters) < 1:
    print('YES')
elif len(letters) == 1:
    key, value = letters.popitem()
    if value == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')