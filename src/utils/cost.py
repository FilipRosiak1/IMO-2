def calculate_cost(cycle, distance_matrix):
    total_cost = 0
    
    for i in range(len(cycle) - 1):
        total_cost += distance_matrix[cycle[i]][cycle[i+1]]

    total_cost += distance_matrix[cycle[0]][cycle[-1]]

    return  total_cost


def calculate_total_cost(cycle1, cycle2, distance_matrix):
    cycle1_cost = calculate_cost(cycle1, distance_matrix)
    cycle2_cost = calculate_cost(cycle2, distance_matrix)

    total = cycle1_cost + cycle2_cost

    return cycle1_cost, cycle2_cost, total