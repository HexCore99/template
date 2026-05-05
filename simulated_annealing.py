import math
import random


def get_neighbours(terrain, pos):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rows = len(terrain)
    cols = len(terrain[0])
    neighbours = []
    for x, y in moves:
        dx = pos[0] + x
        dy = pos[1] + y
        if 0 <= dx < rows and 0 <= dy < cols:
            neighbours.append((dx, dy))
    return neighbours


def simulated_annealing(terrain, st, goal, maxTemp, minTemp, coolingRate):
    currVal = bestVal = terrain[st[0]][st[1]]
    currPos = bestPos = st
    while maxTemp > minTemp:
        if currPos == goal:
            print("found goal")
            break

        neighbours = get_neighbours(terrain, currPos)
        if not neighbours:
            break
        next_pos = random.choice(neighbours)
        next_val = terrain[next_pos[0]][next_pos[1]]
        delta = next_val - currVal

        if delta > 0:
            currVal = next_val
            currPos = next_pos

        else:
            probability = math.exp(delta / maxTemp)
            if random.random() < probability:
                currPos = next_pos
                currVal = next_val
        if currVal > bestVal:
            bestVal = currVal
            bestPos = currPos

        maxTemp *= coolingRate

    print(bestPos)
    print(bestVal)


if __name__ == "__main__":
    terrain = [[10, 12, 14, 13], [11, 15, 18, 16], [9, 14, 20, 17], [8, 13, 19, 21]]
    simulated_annealing(terrain, (0, 0), (3, 3), 100, 0.1, 0.99)
