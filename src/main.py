from utils.load_data import get_instance, read_data
from starting_algorithms.random_cycle import initial_random
from starting_algorithms.greedy_nn import initial_greedy
from algorithms.random_walk import random_walk
from algorithms.greedy_local_search import greedy_local_search
from algorithms.steepest_local_search import steepest_local_search
import time
import numpy as np
import matplotlib.pyplot as plt
import os


RUNS = 100
INSTANCES = ["data/kroA200.tsp", "data/kroB200.tsp"]
INSTANCES = ["data/kroB200.tsp"]

def run_experiment(distance_matrix, initialization="random"):
    results = {alg: [] for alg in ["Steepest_V", "Steepest_E", "Greedy_V", "Greedy_E"]}
    times = {alg: [] for alg in results}

    for i in range(RUNS):
        print(f"Inter {i+1}")

        if initialization == "random":
            cycle1, cycle2 = initial_random(distance_matrix)
        else:
            cycle1, cycle2 = initial_greedy(distance_matrix)

        for alg, search_func, swap_type in [
            ("Steepest_V", steepest_local_search, "vertices"),
            ("Steepest_E", steepest_local_search, "edges"),
            ("Greedy_V", greedy_local_search, "vertices"),
            ("Greedy_E", greedy_local_search, "edges")
        ]:
            start_time = time.time()
            best_cycles, best_costs = search_func(cycle1, cycle2, distance_matrix, swap_type)

            stop_time = time.time() - start_time
            print(stop_time)

            times[alg].append(stop_time)
            results[alg].append((best_cycles, best_costs))

    return results, times


def run_baseline(distance_matrix, max_time):
    
    results = {"Random_Walk": []}
    times = {"Random_Walk": []}

    for i in range(RUNS):
        print(f"Inter {i+1}")

        cycle1, cycle2 = initial_random(distance_matrix)
        start_time = time.time()
        best_cycles, best_costs = random_walk(cycle1, cycle2, distance_matrix, max_time)

        stop_time = time.time() - start_time
        print(stop_time)

        times["Random_Walk"].append(stop_time)
        results["Random_Walk"].append((best_cycles, best_costs))

    return results, times


def print_results(results, times, instance_name):
    print(f"\n=== Results for {instance_name} ===")
    print("\n**Objective Function Values**")
    print(f"{'Algorithm':<12} {'Min':<10} {'Max':<10} {'Mean':<10}")
    for alg, values in results.items():
        costs = [value[1][2] for value in values]
        print(f"{alg:<12} {min(costs):<10} {max(costs):<10} {np.mean(costs):<10.2f}")

    print("\n**Execution Times (s)**")
    print(f"{'Algorithm':<12} {'Min':<10} {'Max':<10} {'Mean':<10}")
    for alg, values in times.items():
        print(f"{alg:<12} {min(values):<10.2f} {max(values):<10.2f} {np.mean(values):<10.2f}")


def plot_results(data, results, instance):
    for algorithm, runs in results.items():
        best_index = min(range(len(runs)), key=lambda i: runs[i][1][2])
        best_cycles, best_costs = runs[best_index]

        instance_name = f"{instance}_{algorithm}_Best"
        plot_result(data, best_cycles[0], best_cycles[1], instance_name)


def plot_result(data, cycle1, cycle2, save_path):
    x = [city.x for city in data]
    y = [city.y for city in data]

    plt.scatter(x, y)
    cycle1_x = [data[i].x for i in cycle1] + [data[cycle1[0]].x]
    cycle1_y = [data[i].y for i in cycle1] + [data[cycle1[0]].y]
    plt.plot(cycle1_x, cycle1_y, 'r', label="Cycle 1")

    cycle2_x = [data[i].x for i in cycle2] + [data[cycle2[0]].x] 
    cycle2_y = [data[i].y for i in cycle2] + [data[cycle2[0]].y]
    plt.plot(cycle2_x, cycle2_y, 'b', label="Cycle 2")

    
    dir_name = os.path.dirname(save_path)
    if dir_name and not os.path.exists(dir_name):
        os.mkdir(save_path)
    plt.savefig(save_path)

    plt.close()



if __name__ == "__main__":
    for instance in INSTANCES:
        data = read_data(instance)
        distance_matrix = get_instance(instance)
        instance_name = instance.split('/')[1]

        print(f"\nRunning Experiment on {instance} (Random Initialization)")
        random_results, random_times = run_experiment(distance_matrix, "random")
        print_results(random_results, random_times, instance)
        plot_results(data, random_results, f"data/plots/random_{instance_name[:-4]}")

        print(f"\nRunning Experiment on {instance} (Greedy Initialization)")
        greedy_results, greedy_times = run_experiment(distance_matrix, "greedy")
        print_results(greedy_results, greedy_times, instance)
        plot_results(data, greedy_results, f"data/plots/greedy_{instance_name[:-4]}")

        print(f"\nRunning Experiment on {instance} (Random Walk)")
        max_time1, max_time2 = 0, 0
        for alg, values in random_times.items():
            max_time1 = max(max_time1, np.mean(values))

        for alg, values in greedy_times.items():
            max_time2 = max(max_time2, np.mean(values))

        max_time = max(max_time1, max_time2)

        baseline_results, baseline_times = run_baseline(distance_matrix, max_time)
        print_results(baseline_results, baseline_times, instance)
        plot_results(data, baseline_results, f"data/plots/{instance_name[:-4]}")



    
