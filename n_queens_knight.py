import random


def get_Location(board, currPos):
    # moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    moves = [(-2, 1), (-2, -1), (1, -2), (-1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]
    n = len(board)
    locations = []
    for x, y in moves:
        dx = currPos[0] + x
        dy = currPos[1] + y
        if 0 <= dx < n and 0 <= dy < n:
            locations.append((dx, dy))
    return locations


def check_attacking(board, location):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    n = len(board)

    for move in moves:
        dx = location[0] + move[0]
        dy = location[1] + move[1]
        while 0 <= dx < n and 0 <= dy < n:
            if board[dx][dy] == "Q":
                return True
            dx = dx + move[0]
            dy = dy + move[1]
    return False


def place_queens(n):
    board = []
    placed = False

    cnt = 0
    while cnt != n:
        board = [["." for _ in range(n)] for _ in range(n)]
        currPos = (random.randint(0, n - 1), random.randint(0, n - 1))
        board[currPos[0]][currPos[1]] = "Q"
        cnt = 1
        while cnt != n:
            locations = get_Location(board, currPos)
            placed = False
            print(locations)

            for locate in locations:
                if board[locate[0]][locate[1]] == "." and not check_attacking(
                    board, locate
                ):
                    board[locate[0]][locate[1]] = "Q"
                    currPos = locate
                    cnt = cnt + 1
                    placed = True
                    break
            if not placed:
                break

    for row in board:
        print(row)


if __name__ == "__main__":
    N = int(input("Enter Number of queens: "))
    place_queens(N)
