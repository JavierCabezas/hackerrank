class Stack:
    def __init__(self):
        self.items = []
        self.max_array = []

    def push(self, item):
        self.items.append(item)
        if len(self.max_array) == 0:
            self.max_array.append(item)
        elif self.max_array[-1] < item:
            self.max_array.append(item)
        else:
            self.max_array.append(self.max_array[-1])
    def pop(self):
        self.items.pop()
        self.max_array.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def peek_max(self):
        return self.max_array[-1]

s = Stack()
number_commands = int(input())
lines = [ list(map(int, input().strip().split(' '))) for _ in range(number_commands) ]

for line in lines:
    if(line[0] == 1):
        s.push(line[1])
    elif(line[0] == 2):
        s.pop()
    elif(line[0] == 3):
        print(s.peek_max())