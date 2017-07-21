_ = int(input())
candidates = sorted([int(x) for x in input().split(" ")], reverse=True)

solution_found = False
for i in range(len(candidates) - 2):
    if candidates[i] < (candidates[i+1] + candidates[i+2]) and not solution_found:
        print (candidates[i+2], candidates[i+1], candidates[i])
        solution_found = True

if not solution_found:
    print(-1)