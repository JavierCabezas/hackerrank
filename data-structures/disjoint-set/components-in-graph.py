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

for node in nodes:
