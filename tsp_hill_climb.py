import random


def calculate_cost(distance_matrix, cities):
    cost = 0
    n = len(cities)
    for col in range(n):
        row = (col + 1) % n
        cost += distance_matrix[cities[col]][cities[row]]

    return cost


def get_neighbours(distance_matrix, cities):
    best_paths = []
    curr_cost = calculate_cost(distance_matrix, cities)
    best_cost = curr_cost
    n = len(cities)

    for st in range(n):
        for curr in range(st + 1, n):
            new_path = cities[:]
            new_path[st] = cities[curr]
            new_path[curr] = cities[st]
            new_cost = calculate_cost(distance_matrix, new_path)
            if new_cost < best_cost:
                best_cost = new_cost
                best_paths = [new_path]
            elif new_cost == best_cost:
                best_paths.append(new_path)

    return best_paths, best_cost


def tsp(distance_matrix, st):
    cities = [0, 1, 3, 2]
    while True:
        curr_cost = calculate_cost(distance_matrix, cities)

        cities_list, best_cost = get_neighbours(distance_matrix, cities)
        if best_cost >= curr_cost:
            break
        cities = random.choice(cities_list)

    print(cities)
    print(calculate_cost(distance_matrix, cities))


# distance_matrix = [[0, 4, 8, 10], [4, 0, 7, 6], [8, 7, 0, 5], [10, 6, 5, 0]]
distance_matrix = [[0, 2, 9, 10], [1, 0, 6, 4], [15, 7, 0, 8], [6, 3, 12, 0]]
tsp(distance_matrix, 0)
