import sys
sys.setrecursionlimit(15000)

class Graph:
    def __init__(self, value):
        self.value = value
        self.nodes = []
        self.was_visited = False

    def add_vertice(self, node):
        self.nodes.append(node)
        node.nodes.append(self)

number_of_inputs = int(input())
vertices = [ list(map(int, input().split(" "))) for _ in range(number_of_inputs)]
nodes = {}

for vertix in vertices:
    first_node_value = vertix[0]
    second_node_value = vertix[1]

    if not first_node_value in nodes:
        nodes[first_node_value] = Graph(first_node_value)
    if not second_node_value in nodes:
        nodes[second_node_value] = Graph(second_node_value)

    nodes[first_node_value].add_vertice(nodes[second_node_value])

def count_connected_nodes(father_node):
    if father_node.was_visited:
        return 0

    father_node.was_visited = True
    count = 1

    for brother in father_node.nodes:
        if not brother.was_visited:
            count += count_connected_nodes(brother)

    return count

vertices = []
for node in nodes.values():
    connected = count_connected_nodes(node)
    if connected > 0:
        vertices.append(connected)

print("{} {}".format(min(vertices), max(vertices)))