from functools import reduce
from operator import xor

i_dont_need_you = int(input())
numbers = list(map(int, input().split(" ")))

print(reduce(lambda x,y: xor(x, y), numbers))