number_of_numbers = int(input())
number_list = [int(input()) for _ in range(number_of_numbers)]

for numb in number_list:
    number_of_digits = 0
    digit_list = [int(x) for x in str(numb)]
    for digit in digit_list:
        if digit > 0 and numb % digit == 0:
            number_of_digits += 1
    print(number_of_digits)
