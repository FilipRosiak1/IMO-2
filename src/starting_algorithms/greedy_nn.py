import random

def initial_greedy(distance_matrix):
    n = len(distance_matrix)

    nodes = list(range(n))

    cycle1 = []
    cycle2 = []

    cycle1.append(random.choice(nodes))
    nodes.remove(cycle1[0])

    cycle2.append(random.choice(nodes))
    nodes.remove(cycle2[0])

    current_node1 = cycle1[0]
    current_node2 = cycle2[0]
    while nodes:
        nearest_node1 = min(((node, distance_matrix[current_node1][node]) for node in nodes), key=lambda x: x[1])[0]
        cycle1.append(nearest_node1)
        nodes.remove(nearest_node1)
        current_node1 = nearest_node1

        if nodes:
            nearest_node2 = min(((node, distance_matrix[current_node2][node]) for node in nodes), key=lambda x: x[1])[0]
            cycle2.append(nearest_node2)
            nodes.remove(nearest_node2)
            current_node2 = nearest_node2

    return cycle1, cycle2