import sys

def inside(r, c, n):
    return (0 <= r < n) and (0 <= c < n)

def can_place(board, n, (row, col)):
    rng = range(1, row+1)
    if any(board[row - i][col - i] for i in rng if 0 <= row-i < n and 0 <= col-i < n):
        return False
    if any(board[row - i][col + i] for i in rng if 0 <= row-i < n and 0 <= col+i < n):
        return False
    if any(board[row - i][col] for i in rng):
        return False
    return True

def place_queens(board, n=None, row=0, good_columns=None, bad_columns=None):
    if n is None:
        n = len(board)
    if good_columns is None:
        good_columns = set(range(n))
    if bad_columns is None:
        bad_columns = set()

    all_cols = set(range(n))

    for col in good_columns - bad_columns:
        if can_place(board, n, (row, col)):
            board[row][col] = 1
            if row == n - 1:
                return True
            bad_cols = {col + x for x in (-1, 0, 1) if 0 <= col + x < n} | bad_columns
            good_cols = all_cols - bad_cols
            if place_queens(board, n, row + 1, good_cols, bad_columns | {col}):
                return True
            board[row][col] = 0
    return False


def main():
    n = int(sys.argv[1])
    board = [[0]*n for _ in range(n)]
    if place_queens(board):
        print "--"
        print "\n".join(str(r) for r in board)
    else:
        print "Can't place.."

if __name__ == '__main__':
    main()
