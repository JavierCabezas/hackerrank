class Hourglass:
    def __init__(self, hourglass_arr):
        self.hourglass = hourglass_arr
        self.matrix_size = len(self.hourglass)

    def calculate_hourglass(self, x, y):
        return self.hourglass[y - 1][x - 1] + \
               self.hourglass[y - 1][x] + \
               self.hourglass[y - 1][x + 1] + \
               self.hourglass[y][x] + \
               self.hourglass[y + 1][x - 1] + \
               self.hourglass[y + 1][x] + \
               self.hourglass[y + 1][x + 1]

    def get_current_max(self):
        current_max = -9*9
        for x in range(1, self.matrix_size - 1):
            for y in range(1, self.matrix_size - 1):
                current_max = max(self.calculate_hourglass(x, y), current_max)
        return current_max


MATRIX_SIZE = 6
matrix = [
    [int(x) for x in input().split()] for i in range(0, MATRIX_SIZE)
]
hourglass = Hourglass(matrix)
print(hourglass.get_current_max())
