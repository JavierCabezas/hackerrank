temp = input().split(" ")
n = int(temp[0]) #Number of different flowers
k = int(temp[1]) #Number of friends that are going to buy them
costs = [int(x) for x in input().split(" ")]
costs.sort()

flowers_per_person = [n//k for i in range(k)]
flowers_remaining = n - k*(n//k)

for i in range(flowers_remaining):
    flowers_per_person[i] += 1

total = 0
for flowers_to_take in flowers_per_person:
    x = 0
    if flowers_to_take == 0:
        break

    #take the most expensive flower first
    total += costs[-1]
    del costs[-1]
    if flowers_to_take > 1:
        mult = 1
        #take N, giving priority to the cheapest ones.
        for cost in reversed(costs[:(flowers_to_take-1)]):
            total += (mult+1)*cost
            mult += 1
        del costs[:(flowers_to_take-1)]


print(total)