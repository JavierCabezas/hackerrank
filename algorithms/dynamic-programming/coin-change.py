#total_ammount = int(input().split(" ")[0])
#avaiable_coins = list(map(int, input().split(" ")))

combinations = []

avaiable_coins = [1, 2, 5]
avaiable_coins.sort()
max_coin = max(avaiable_coins)
min_coin = min(avaiable_coins)


def coin_combinations(remaining, last_index):
    if remaining == 0:
        return 1

    total = 0

    for i, coin in enumerate(avaiable_coins[last_index:]):
        if remaining >= coin:
            total += coin_combinations(
                remaining - coin,
                i
            )

    return total

print(coin_combinations(5, 0))