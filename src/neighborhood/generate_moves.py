from typing import Literal
from .inter_cycle import inter_cycle_swap_cost
from .intra_cycle import intra_cycle_vertice_swap_cost, intra_cycle_edge_swap_cost

def generate_moves(cycles, costs, distance_matrix, swap_type: Literal["vertices", "edges"]):
    neighborhood = []

    for i in range(len(cycles[0])):
        for j in range(len(cycles[1])):

            d1, d2 = inter_cycle_swap_cost(cycles[0], cycles[1], i, j, distance_matrix)

            new_costs = [costs[0] + d1, costs[1] + d2, costs[2] + d1 + d2]

            neighborhood.append([None, None, i, j, new_costs])
    

    for cycle_num in range(len(cycles)):
        for i in range(len(cycles[cycle_num])):
            for j in range(i, len(cycles[cycle_num])):

                if swap_type == "vertices":
                    d = intra_cycle_vertice_swap_cost(cycles[cycle_num], i, j, distance_matrix)
                elif swap_type == "edges":
                    d = intra_cycle_edge_swap_cost(cycles[cycle_num], i, j, distance_matrix)

                new_costs = costs.copy()
                new_costs[cycle_num] += d
                new_costs[2] += d

                neighborhood.append([swap_type, cycle_num, i, j, new_costs])

    return neighborhood