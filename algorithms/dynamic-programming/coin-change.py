import sys

total_ammount = int(input().split(" ")[0])
avaiable_coins = list(map(int, input().split(" ")))
avaiable_coins.sort()
sys.setrecursionlimit(6000)

class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


@memoize
def coin_combinations(remaining, last_index):
    if remaining == 0:
        return 1

    total = 0

    for i, coin in enumerate(avaiable_coins[last_index:]):
        if remaining >= coin:
            out = coin_combinations(
                remaining - coin,
                i + last_index,
            )
            if out is not None:
                total += out

    return total

print(coin_combinations(total_ammount, 0))