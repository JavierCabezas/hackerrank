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
repeat_tax = [0] * k
for i in range(n):
    person_index = i % k
    if flowers_per_person[person_index ] > 0:
        flowers_per_person[person_index] -= 1
        #Always take first the most expensive flower
        total += ( costs[-1] * (repeat_tax[person_index] + 1) )
        del costs[-1]
        repeat_tax[person_index] += 1

print(total)