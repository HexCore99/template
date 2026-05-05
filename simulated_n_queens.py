import math
import random


def count_attacks(queens):
    n = len(queens)
    attacks = 0

    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j]:
                attacks += 1
            if abs(queens[i] - queens[j]) == abs(i - j):
                attacks += 1

    return attacks


def get_random_neighbour(queens):
    n = len(queens)
    neighbour = queens[:]
    col = random.randint(0, n - 1)
    row = random.randint(0, n - 1)
    while row == queens[col]:
        row = random.randint(0, n - 1)

    neighbour[col] = row
    return neighbour


def simulated_annealing(n):
    temp = 1000
    cooling_rate = 0.995
    min_temp = 0.001
    queens = [random.randint(0, n - 1) for _ in range(n)]
    while temp > min_temp:
        curr_attacks = count_attacks(queens)
        if curr_attacks == 0:
            return queens

        neighbour = get_random_neighbour(queens)
        new_attacks = count_attacks(neighbour)

        delta = new_attacks - curr_attacks
        if delta < 0:
            queens = neighbour
        else:
            probability = math.exp(-delta / temp)
            if random.random() < probability:
                queens = neighbour
        temp *= cooling_rate
    return None


def place_queens(n):

    for i in range(1000):
        result = simulated_annealing(n)
        if result:
            print(f"Solve  {result}")
            return result
    print("No solution found.")
    return None


N = int(input("Enter Number of queens: "))
place_queens(N)
