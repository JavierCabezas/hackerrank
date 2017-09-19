from collections import namedtuple
IceCreamTrip = namedtuple('IceCreamTrip', 'money, quantity, ice_cream_prices')
cases = []

number_of_tescases = int(input())
for _ in range(number_of_tescases):
    money, quantity = int(input()), int(input())
    prices = list(map(int, input().split(" ")))
    cases.append(IceCreamTrip(money=money, quantity=quantity, ice_cream_prices=prices))

def check(case):
    stored_prices = {}
    for idx, price in enumerate(case.ice_cream_prices):
        remaining = case.money - price
        if remaining in stored_prices:
            initial_index = idx +1
            last_index = stored_prices[remaining] + 1
            return [initial_index, last_index]
        else:
            stored_prices[price] = idx


for case in cases:
    idxs = check(case)
    print(idxs[1], idxs[0])