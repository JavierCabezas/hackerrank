#snakes and ladders
class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []
    def add_connection(self, Node, weight):
        self.connections.append((Node, weight))

nodes = {}

number_of_testcases = int(input())
for _ in range(number_of_testcases):
    snake_or_ladder = []
    number_of_ladders = int(input())
    for __ in range(number_of_ladders):
        snake_or_ladder.append(tuple(map(int, input().split(" "))))
    number_of_snakes = int(input())
    for __ in range(number_of_snakes):
        snake_or_ladder.append(tuple(map(int, input().split(" "))))

    del nodes
    nodes = {1: Node(1), 100: Node(100) }

    for i in range(2, 100):
        nodes[i] = Node(i)
        # Connect all nodes with a weight of 1
        nodes[i-1].add_connection(nodes[i], 1)

    for sol in snake_or_ladder:
        start = sol[0]
        end = sol[1]

        nodes[start].add_connection(nodes[end], start-end)

