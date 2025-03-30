from utils.cost import calculate_total_cost
from neighborhood.generate_moves import generate_moves
from neighborhood.intra_cycle import intra_cycle_edge_swap_move, intra_cycle_vertice_swap_move
from neighborhood.inter_cycle import inter_cycle_swap_move
from typing import Literal

def steepest_local_search(cycle1, cycle2, distance_matrix, swap_type: Literal["vertices", "edges"]):
    best_cycles = [cycle1.copy(), cycle2.copy()]
    best_costs = list(calculate_total_cost(cycle1, cycle2, distance_matrix))

    while True:
        neighborhood = generate_moves(best_cycles, best_costs, distance_matrix, swap_type)

        best_move = min(neighborhood, key=lambda x: x[4][2])

        if best_move[4][2] >= best_costs[2]:
            break

        what_swap, cycle_num, i, j, new_costs = best_move

        best_costs = new_costs

        if what_swap == "vertices":
            intra_cycle_vertice_swap_move(best_cycles[cycle_num], i, j)
        elif what_swap == "edges":
            intra_cycle_edge_swap_move(best_cycles[cycle_num], i, j)
        else:
            inter_cycle_swap_move(best_cycles[0], best_cycles[1], i, j)

    return best_cycles, best_costs


        
