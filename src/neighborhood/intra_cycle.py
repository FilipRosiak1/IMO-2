def intra_cycle_vertice_swap_cost(cycle, i, j, distance_matrix):
    if abs(i - j) == 1 or (i == 0 and j == len(cycle) - 1) or (i == len(cycle) - 1 and j == 0) or (i == j):
        return 0
    
    prev_node1 = cycle[i - 1]
    next_node1 = cycle[(i + 1) % len(cycle)]

    prev_node2 = cycle[j - 1]
    next_node2 = cycle[(j + 1) % len(cycle)]

    delta = -distance_matrix[prev_node1][cycle[i]] - distance_matrix[cycle[i]][next_node1] + \
                distance_matrix[prev_node1][cycle[j]] + distance_matrix[cycle[j]][next_node1] - \
                distance_matrix[prev_node2][cycle[j]] - distance_matrix[cycle[j]][next_node2] + \
                distance_matrix[prev_node2][cycle[i]] + distance_matrix[cycle[i]][next_node2]
    
    return delta

def intra_cycle_vertice_swap_move(cycle, i, j):
    if abs(i - j) == 1 or (i == 0 and j == len(cycle) - 1) or (i == len(cycle) - 1 and j == 0) or (i == j):
        return
    
    cycle[i], cycle[j] = cycle[j], cycle[i]


def intra_cycle_edge_swap_cost(cycle, i, j, distance_matrix):
    if abs(i - j) == 1 or (i == 0 and j == len(cycle) - 1) or (i == len(cycle) - 1 and j == 0) or (i == j):
        return 0
    
    if i > j:
        i, j = j, i
    
    delta_neg = distance_matrix[cycle[j]][cycle[(j + 1) % len(cycle)]] + distance_matrix[cycle[i]][cycle[(i + 1) % len(cycle)]]
    delta_pos = distance_matrix[cycle[j]][cycle[i]] + distance_matrix[cycle[(j + 1) % len(cycle)]][cycle[(i + 1) % len(cycle)]]
    delta = delta_pos - delta_neg

    return delta

def intra_cycle_edge_swap_move(cycle, i, j):
    if abs(i - j) == 1 or (i == 0 and j == len(cycle) - 1) or (i == len(cycle) - 1 and j == 0) or (i == j):
        return
    
    if i > j:
        i, j = j, i
    
    cycle[(i + 1) % len(cycle)], cycle[j] = cycle[j], cycle[(i + 1) % len(cycle)]

    if i < j:
        cycle[(i + 2) % len(cycle):j] = cycle[(i + 2) % len(cycle):j][::-1]
    else:
        reversed_part = cycle[i + 2:] + cycle[:j]
        reversed_part.reverse()
        cycle[i + 2:], cycle[:j] = reversed_part[:len(cycle[i + 2:])], reversed_part[len(cycle[i + 2:]):]
