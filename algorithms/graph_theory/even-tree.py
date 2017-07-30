class Node:
    def __init__(self, value, sons = []):
        self.value = value
        self.sons = []
        self.has_parent = False
        for son in sons:
            self.sons.append(son)

    def add_son(self, node):
        self.sons.append(node)
        node.has_parent = True

    def delete_son_by_value(self, value):
        for s in self.sons:
            if s.value == value:
                #print("Removed link from parent {} to son {}".format(self.value, s.value))
                s.has_parent = False #  ='(
                self.sons.remove(s)
                return True
        return False

    def number_of_sons(self):
        return len(self.sons)

    def nodes_in_tree_with_this_root(self):
        node_number = 1
        for son in self.sons:
            node_number += son.nodes_in_tree_with_this_root()
        return node_number

    def remove_extra_nodes(self):
        nodes_per_tree = {}
        removed = 0
        for son in self.sons: #We sum all the nodes that are under this one.
            nodes_per_tree[son.value] = son.nodes_in_tree_with_this_root()
        total_nodes = sum(nodes_per_tree.values()) + 1 #add the parent
        if self.has_parent:
            total_nodes += 1 #If this node still has a parent we should add this one in the sum because they are still connected

        if total_nodes % 2 == 0:
            for node_value, number_of_sons in nodes_per_tree.items():
                if number_of_sons % 2 == 0 and number_of_sons > 0:  # This node can me safely de-attached from parent
                    self.delete_son_by_value(node_value)
                    total_nodes -= number_of_sons
                    removed += 1
        return removed



#Read input and create the nodes
nodes = {}
nodes[1] = Node(1)
number_of_nodes = int(input().split(" ")[1])
for i in range(number_of_nodes):
    aux = input().split(" ")
    value, father = int(aux[0]), int(aux[1])
    nodes[value] = Node(value)
    nodes[father].add_son(nodes[value])

#Count the number of nodes removed
removed_nodes = 0
for node_id, node in nodes.items():
    removed_nodes += node.remove_extra_nodes()
print(removed_nodes)
