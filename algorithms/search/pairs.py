i_wont_use_you, difference = map(int, input().split(" "))
dict = {}
numbers_to_check = list(map(int, input().split(" ")))

for n in numbers_to_check:
    dict[n] = 0

differences_found = 0
for n in numbers_to_check:
    if n+difference in dict:
        differences_found +=1

print(differences_found)