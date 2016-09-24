import sys
import random

def can_place(board, n, (row, col)):
    rng = range(2, row+1) #No need to check the immediate row above. 
    if any(board[row - i][col - i] for i in rng if 0 <= row-i < n and 0 <= col-i < n):
        return False
    if any(board[row - i][col + i] for i in rng if 0 <= row-i < n and 0 <= col+i < n):
        return False
    #No need to check columns, just diagonals is fine.
    return True

def place_queens(board, n, all_cols, row, good_columns, bad_columns):
    cols = list(good_columns - bad_columns)
    random.shuffle(cols)
    for col in cols:
        if can_place(board, n, (row, col)):
            board[row][col] = 1
            if row == n - 1:
                return True
            bad_cols = {x for x in (col - 1, col, col + 1) if 0 <= x < n} | bad_columns
            good_cols = all_cols - bad_cols
            if place_queens(board, n, all_cols, row + 1, good_cols, bad_columns | {col}):
                return True
            board[row][col] = 0
    return False

def main():
    n = int(sys.argv[1])
    board = [[0]*n for _ in range(n)]
    if place_queens(board, n, set(range(n)), 0, set(range(n)), set()):
        print "\n".join(str(r) for r in board)
    else:
        print "Can't place.."

if __name__ == '__main__':
    main()
