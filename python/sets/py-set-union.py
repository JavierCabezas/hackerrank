dont_need_you = input()
first_set = set([int(x) for x in input().split(" ")])
dont_need_you = input()
second_set = set([int(x) for x in input().split(" ")])

print(len(first_set.union(second_set)))