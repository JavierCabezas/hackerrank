number_of_elements = int(input())
steps = input()

UPHILL = 'U'
DOWNHILL = 'D'
height = 0
valleys = 0

for step in steps:
    if step == UPHILL:
        height += 1
        if height == 0:
            valleys += 1
    elif step == DOWNHILL:
        height -= 1

print(valleys)