number, pow = int(input()), int(input())

def pow_combinations(number, starting_from):
    if number == 0:
        return 1

    result = 0
    for i in range(starting_from, number):
        current = i**pow
        if not current > number:
            result += pow_combinations(number-current, i+1)

    return result

print(pow_combinations(number, 1))