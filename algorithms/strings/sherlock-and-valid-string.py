string_to_check = input()

times_that_each_character_is_repeated = {}
frecuencies_in_word = {}
frecuencies = []

for char in string_to_check:
    if not char in times_that_each_character_is_repeated:
        times_that_each_character_is_repeated[char] = 0
    times_that_each_character_is_repeated[char] += 1

for c in times_that_each_character_is_repeated:
    quantity = times_that_each_character_is_repeated[c]
    if not quantity in frecuencies_in_word:
        frecuencies_in_word[quantity] = 0
        frecuencies.append(quantity)
    frecuencies_in_word[quantity] += 1

print(frecuencies)
print(frecuencies_in_word)
if len(frecuencies) == 1:
    print("YES")
elif len(frecuencies) > 2:
    print("NO")
else:
    difference = frecuencies_in_word[frecuencies[0]] - frecuencies_in_word[frecuencies[1]]
    print("YES" if difference <= 0 else "NO")