i_wont_use_you = int(input())
toy_weights = list(map(int, input().split(" ")))
toy_weights.sort()

toys_to_buy = 0
current = -5

for w in toy_weights:
    if w > current + 4:
        current = w
        toys_to_buy += 1

print(toys_to_buy)