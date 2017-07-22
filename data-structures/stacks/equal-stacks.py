class Stack:
    def __init__(self, items_to_add):
        self.items = []
        self.height = 0
        for item in reversed(items_to_add):
            self.push(item)
    def push(self, item):
        self.items.append(item)
        self.height += item
    def pop(self):
        self.height -=  self.items.pop()
    def peek_heigth(self):
        return self.height
    def remove_if_bigger(self, value):
        if value <= self.height:
            self.pop()

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

stack1, stack2, stack3 = Stack(h1), Stack(h2), Stack(h3)

while not (stack1.peek_heigth() == stack2.peek_heigth() == stack3.peek_heigth()):
    max_h = max(stack1.peek_heigth(), stack2.peek_heigth(), stack3.peek_heigth())
    stack1.remove_if_bigger(max_h)
    stack2.remove_if_bigger(max_h)
    stack3.remove_if_bigger(max_h)

print(stack1.height)

