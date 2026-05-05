def hill_climbing(terrain, st, goal):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    rows = len(terrain)
    cols = len(terrain[0])

    # assuming squared shape field
    valueNpos = (terrain[st[0]][st[1]], st)
    value = None
    pos = None
    while valueNpos:
        value = valueNpos[0]
        pos = valueNpos[1]
        valueNpos = None
        for i in move:
            dr, dc = i
            nr = pos[0] + dr
            nc = pos[1] + dc
            print(dr)
            print(dc)
            print()
            if 0 <= nr < rows and 0 <= nc < cols and value < terrain[nr][nc]:
                valueNpos = (terrain[nr][nc], (nr, nc))
    print(value)
    print(pos)


if __name__ == "__main__":
    print("all good")
    terrain = [[10, 12, 14, 13], [11, 15, 18, 16], [9, 14, 20, 17], [8, 13, 19, 21]]
    hill_climbing(terrain, (0, 0), (3, 3))
