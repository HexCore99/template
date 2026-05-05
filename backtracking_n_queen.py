def is_safe(board, row, col, n):
    # check column
    for r in range(row):
        if board[r][col] == "Q":
            return False

    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False
        r -= 1
        c -= 1

    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        if board[r][c] == "Q":
            return False
        r -= 1
        c += 1

    return True


def place_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            if place_queens(board, row + 1, n):
                return True

            board[row][col] = "."

    return False


if __name__ == "__main__":
    n = int(input("Enter Number of queens: "))
    board = [["." for _ in range(n)] for _ in range(n)]
    if place_queens(board, 0, n):
        for row in board:
            print(row)
