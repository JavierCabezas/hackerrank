number_of_tests = int(input())

for iterator in range(0, number_of_tests):
    i_dont_need_you = int(input())
    candidate_group = [int(n) for n in input().split(" ")]
    i_also_dont_need_you = int(input())
    target_group = [int(n) for n in input().split(" ")]

    is_subgroup = True
    for candidate in candidate_group:
        if candidate not in target_group:
            is_subgroup = False
            break

    print(str(is_subgroup))
