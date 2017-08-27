orders = {}

number_of_orders = int(input())
for order_number in range(1, number_of_orders+1):
    finished_in = sum(map(int, input().split(" ")))
    orders[order_number] = finished_in

s = [k for k in sorted(orders, key=orders.get)]
for k in s:
    print(k, end=" ")