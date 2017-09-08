from math import sqrt, ceil

to_encrypt = input().replace(" ", "")

min = int(sqrt(len(to_encrypt)))
max = ceil(sqrt(len(to_encrypt)))

matrix = []
while len(to_encrypt) > 0:
    matrix.append(to_encrypt[0:(min+1)])
    to_encrypt = to_encrypt[(min+1):]


for col in range(max):
    for row in range(len(matrix)):
        try:
            print(matrix[row][col], end='')
        except:
            pass
    print(" ", end='')