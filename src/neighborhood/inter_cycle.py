def inter_cycle_swap_cost(cycle1, cycle2, i, j, distance_matrix):
    prev_node1 = cycle1[i - 1]
    next_node1 = cycle1[(i + 1) % len(cycle1)]

    prev_node2 = cycle2[j - 1]
    next_node2 = cycle2[(j + 1) % len(cycle2)]

    delta1 = -distance_matrix[prev_node1][cycle1[i]] - distance_matrix[cycle1[i]][next_node1] + \
                distance_matrix[prev_node1][cycle2[j]] + distance_matrix[cycle2[j]][next_node1]
    
    delta2 = -distance_matrix[prev_node2][cycle2[j]] - distance_matrix[cycle2[j]][next_node2] + \
                distance_matrix[prev_node2][cycle1[i]] + distance_matrix[cycle1[i]][next_node2]
    
    return delta1, delta2

def inter_cycle_swap_move(cycle1, cycle2, i, j):
    cycle1[i], cycle2[j] = cycle2[j], cycle1[i]