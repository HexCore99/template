import math
import random


def calculate_cost(distance_matrix, cities):
    cost = 0
    n = len(cities)
    for col in range(n):
        row = (col + 1) % n
        cost += distance_matrix[cities[col]][cities[row]]

    return cost


def get_neighbours(distance_matrix, cities):
    n = len(cities)

    neighbour = cities[:]
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)

    while i == j:
        j = random.randint(0, n - 1)

    neighbour[i] = cities[j]
    neighbour[j] = cities[i]

    return neighbour


def tsp(distance_matrix, st):
    n = len(distance_matrix)
    cities = list(range(n))
    best_route = cities[:]
    best_cost = calculate_cost(distance_matrix, cities)

    temp = 100
    cooling_rate = 0.99
    min_temp = 0.1
    while temp > min_temp:
        curr_cost = calculate_cost(distance_matrix, cities)

        neighbour = get_neighbours(distance_matrix, cities)
        new_cost = calculate_cost(distance_matrix, neighbour)

        delta = new_cost - curr_cost
        if delta < 0:
            cities = neighbour
        else:
            probability = math.exp(-delta / temp)
            if random.random() < probability:
                cities = neighbour
        curr_best_cost = calculate_cost(distance_matrix, cities)
        if curr_best_cost < best_cost:
            best_cost = curr_best_cost
            best_route = cities[:]
        temp *= cooling_rate

    print(best_route)
    print(best_cost)


# distance_matrix = [[0, 4, 8, 10], [4, 0, 7, 6], [8, 7, 0, 5], [10, 6, 5, 0]]
# distance_matrix = [
#     [0, 3, 9, 8, 7, 12, 10, 4],
#     [3, 0, 5, 6, 11, 10, 9, 7],
#     [9, 5, 0, 4, 8, 9, 6, 11],
#     [8, 6, 4, 0, 5, 7, 10, 9],
#     [7, 11, 8, 5, 0, 3, 6, 10],
#     [12, 10, 9, 7, 3, 0, 4, 8],
#     [10, 9, 6, 10, 6, 4, 0, 5],
#     [4, 7, 11, 9, 10, 8, 5, 0],
# ]
distance_matrix = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0],
]
tsp(distance_matrix, 0)
