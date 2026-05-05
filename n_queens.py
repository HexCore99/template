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


def get_best_neighbours(queens):
    n = len(queens)
    best_attacks = current_attacks = count_attacks(queens)
    best_states = []

    for col in range(n):
        original_row = queens[col]
        for row in range(n):
            if original_row == row:
                continue
            queens[col] = row
            current_attacks = count_attacks(queens)
            if current_attacks < best_attacks:
                best_attacks = current_attacks
                best_states = [list(queens)]
            elif current_attacks == best_attacks:
                best_states.append(list(queens))
            queens[col] = original_row
    return best_states, best_attacks


def hill_climbing(n):
    queens = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        curr_attacks = count_attacks(queens)
        if curr_attacks == 0:
            return queens
        neighbours, best_attacks = get_best_neighbours(queens)

        if best_attacks > curr_attacks:
            return None

        queens = random.choice(neighbours)


def place_queens(n, max_restarts=1000):

    for attempt in range(max_restarts):
        result = hill_climbing(n)
        if result:
            print(f"Solved in attempt {attempt + 1}: {result}")
            return result
    print("No solution found.")
    return None


N = int(input("Enter Number of queens: "))
place_queens(N)
