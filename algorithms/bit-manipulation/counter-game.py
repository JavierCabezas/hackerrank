from math import sqrt, log

number_of_tescases = int(input())
games = [int(input()) for _ in range(number_of_tescases)]


def next_turn(n):
    r = log(n, 2)
    n = int(n)
    if r.is_integer():
        return n/2
    else:
        q = int(r)
        return n - (n >> q << q)

for game in games:
    turn = 0
    while game > 1:
        game = next_turn(game)
        turn += 1

    if turn % 2 == 0:
        print('Richard')
    else:
        print('Louise')