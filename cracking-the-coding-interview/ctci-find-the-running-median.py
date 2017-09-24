class Heap:
    def __init__(self):
        self.data = []

    def find_index(self, value_to_add):
        for idx, data in enumerate(self.data):
            if data > value_to_add:
                return idx

        return len(self.data)

    def add_element(self, value_to_add):
        index = self.find_index(value_to_add)
        self.data.insert(index, value_to_add)


    def median(self):
        heap_len = len(self.data)
        if heap_len % 2 == 0 and heap_len > 1:
            return (self.data[int(heap_len/2)] + self.data[int(heap_len/2)-1])/2
        else:
            return self.data[heap_len//2]

h = Heap()
numbers_to_add = [int(input()) for _ in range(int(input()))]

for number in numbers_to_add:
    h.add_element(number)
    print("%.1f" % h.median())