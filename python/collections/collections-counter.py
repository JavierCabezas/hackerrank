number_of_shoes = int(input())
avaiable_shoes = [int(x) for x in input().split(" ")]

number_of_events = int(input())
possible_sales = [ list(map(int, input().split(" "))) for __ in range(number_of_events)]

shoe_dict = {}
for shoe in avaiable_shoes:
    if not shoe in shoe_dict:
        shoe_dict[shoe] = 0
    shoe_dict[shoe] += 1

total_sales = 0
for possible_sale in possible_sales:
    if possible_sale[0] in shoe_dict and shoe_dict[possible_sale[0]] > 0:
        total_sales += possible_sale[1]
        shoe_dict[possible_sale[0]] -= 1

print(total_sales)