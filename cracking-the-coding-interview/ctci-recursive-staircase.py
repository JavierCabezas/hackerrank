number_of_tests = int(input())
steps_per_staircase = [int(input()) for _ in range(number_of_tests)]

step_memory = {}

def count_steps(step):
    count = 0
    if step == 1:
        return 1
    elif step == 2:
        return 2
    elif step == 3:
        return 4
    else:
        #step > 4 from here
        if step in step_memory:
            return step_memory[step]
        steps_if_started_at_1 = step-1
        steps_if_started_at_2 = step-2
        steps_if_started_at_3 = step-3
        count += count_steps(steps_if_started_at_1) + count_steps(steps_if_started_at_2) + count_steps(steps_if_started_at_3)
        step_memory[step] = count
        return count

for step in steps_per_staircase:
    print(count_steps(step))

