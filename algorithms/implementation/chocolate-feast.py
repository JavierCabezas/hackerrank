from collections import namedtuple
Chocoparams = namedtuple('Chocoparams', 'cash, choco_price, wrappers_per_choco')

chococases = []
number_of_trips = int(input())
for _ in range(number_of_trips):
    temp = list(map(int, input().split(" ")))
    chococases.append(Chocoparams(cash=temp[0], choco_price=temp[1], wrappers_per_choco=temp[2]))

current_cash = 0
for case in chococases:
    chocolates_eaten = 0

    #Chocolates bought
    choco_money = case.cash // case.choco_price
    current_wrappers = choco_money
    chocolates_eaten += choco_money

    #chocolates exchanged by wrappers
    while current_wrappers // case.wrappers_per_choco > 0:
        choco_wrappers =  current_wrappers // case.wrappers_per_choco
        chocolates_eaten += choco_wrappers
        current_wrappers = (current_wrappers % case.wrappers_per_choco) + choco_wrappers

    print(chocolates_eaten)
