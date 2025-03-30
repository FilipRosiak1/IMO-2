import time
import random
from utils.cost import calculate_total_cost
from neighborhood.inter_cycle import inter_cycle_swap_cost, inter_cycle_swap_move
from neighborhood.intra_cycle import *

def random_walk(cycle1, cycle2, distance_matrix, time_limit):
    start_time = time.time()

    best_cycles = [cycle1.copy(), cycle2.copy()]
    best_costs = list(calculate_total_cost(cycle1, cycle2, distance_matrix))

    cycles = [cycle1.copy(), cycle2.copy()]
    costs = best_costs.copy()

    while time.time() - start_time < time_limit:

        if random.random() < 0.5:
            i = random.randint(0, len(cycles[0]) - 1)
            j = random.randint(0, len(cycles[1]) - 1)
            d1, d2 = inter_cycle_swap_cost(cycles[0], cycles[1], i, j, distance_matrix)
            inter_cycle_swap_move(cycles[0], cycles[1], i, j)
            costs[0] += d1
            costs[1] += d2
            costs[2] += d1 + d2

            if costs[2] < best_costs[2]:
                best_cycles = [cycles[0].copy(), cycles[1].copy()]
                best_costs = costs.copy()
                
        else:
            cycle_num = random.randint(0, 1)
            i, j = random.sample(range(len(cycles[cycle_num])), 2)

            if random.random() < 0.5:
                d = intra_cycle_vertice_swap_cost(cycles[cycle_num], i, j, distance_matrix)
                intra_cycle_vertice_swap_move(cycles[cycle_num], i, j)
                
            else:
                d = intra_cycle_edge_swap_cost(cycles[cycle_num], i, j, distance_matrix)
                intra_cycle_edge_swap_move(cycles[cycle_num], i, j)
               
            costs[cycle_num] += d
            costs[2] += d

            if costs[2] < best_costs[2]:
                best_cycles = [cycles[0].copy(), cycles[1].copy()]
                best_costs = costs.copy()

    return best_cycles, best_costs




