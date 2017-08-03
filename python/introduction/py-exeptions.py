#Not really an excercise on this section, this is actually the Day 17 of 30 days of code problem
#But this is kind of introductory so I think that it belongs on this section.
number_of_test = int(input())
tests = [ list(map(int, input().split(" "))) for _ in range(number_of_test)]

def do_calculation(n, p):
    if n < 0 or p < 0:
        raise ValueError()
    else:
        return pow(n, p)

for test in tests:
    try:
        print(do_calculation(test[0], test[1]))
    except ValueError:
        print("n and p should be non-negative")