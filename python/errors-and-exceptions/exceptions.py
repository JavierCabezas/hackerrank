def print_div(a, b):
    try:
        div = int(a) // int(b)
        print(div)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code: {}".format(e))

number_of_cases = int(input())
for _ in range(number_of_cases):
    a, b = input().split(" ")
    print_div(a, b)
