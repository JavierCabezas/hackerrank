ENQUEUE = 1
DEQUEUE = 2
PRINT = 3

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
    def switch_stack(self, other_stack):
        while len(self.items) > 0:
            other_stack.push(self.peek())
            self.pop()
    def peek(self):
        return self.items[-1]


def analyze_input(number_of_instructions):
    out = []
    for _ in range(number_of_instructions):
        n = input()
        if int(n[0]) == 1:
            out.append(list(map(int, n.split(" "))))
        else:
            out.append([int(n)])
    return out

instructions = analyze_input(int(input()))
A = Stack()
B = Stack()

for ins in instructions:
    if ins[0] == ENQUEUE:
        A.push(ins[1])
    elif ins[0] == DEQUEUE:
        A.switch_stack(B)
        B.pop()
        B.switch_stack(A)
    elif ins[0] == PRINT:
        A.switch_stack(B)
        print(B.peek())
        B.switch_stack(A)
