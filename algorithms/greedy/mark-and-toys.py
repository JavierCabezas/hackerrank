i_wont_use_you, cash = (int(x) for x in input().split(" "))
toy_values = list(map(int, input().split(" ")))
toy_values.sort()

toys_bought = 0
for val in toy_values:
    if cash - val > 0:
        toys_bought += 1
        cash -= val
    else:
        break

print(toys_bought)