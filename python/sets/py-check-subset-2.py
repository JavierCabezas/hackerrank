number_of_tests = int(input())

for iterator in range(0, number_of_tests):
    _ = int(input())
    candidate_group = set([int(n) for n in input().split(" ")])
    _ = int(input())
    target_group = set([int(n) for n in input().split(" ")])

    print ("True" if target_group >= candidate_group else "False")