persons_per_family = int(input())
rooms = list(int(x) for x in input().split(" "))
unique_rooms = set(rooms)

print( (persons_per_family * sum(unique_rooms) - sum(rooms)) // (persons_per_family - 1) )