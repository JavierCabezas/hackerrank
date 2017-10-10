number_of_lines, items_per_line = input().split(" ")
lines = []
for _ in range(int(number_of_lines)):
    lines.append(list(map(int, input().split(" "))))
k = int(input())

for line in sorted(lines, key=lambda line_row: line_row[k]):
    print(line)