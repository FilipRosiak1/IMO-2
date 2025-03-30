from random import shuffle

def initial_random(distance_matrix):
    n = len(distance_matrix)

    nodes = list(range(n))
    shuffle(nodes)

    cycle1 = nodes[:n // 2]
    cycle2 = nodes[n // 2:]

    return cycle1, cycle2