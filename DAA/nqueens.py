
# N-Queens using Backtracking

def is_safe(board, row, col, N):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, N):

    if row == N:
        return True

    for col in range(N):

        if is_safe(board, row, col, N):

            board[row][col] = 1

            if solve(board, row+1, N):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# User input
N = int(input("Enter number of queens: "))

board = [[0 for j in range(N)] for i in range(N)]

r = int(input("Enter first queen row (1 to N): ")) - 1
c = int(input("Enter first queen column (1 to N): ")) - 1

if not (0 <= r < N and 0 <= c < N):
    print("Invalid position")

else:
    board[r][c] = 1

    if is_safe(board, r, c, N) and solve(board, r+1, N):

        print("\nN-Queens Solution:")
        for row in board:
            print(row)

    else:
        print("No solution exists for this position")
