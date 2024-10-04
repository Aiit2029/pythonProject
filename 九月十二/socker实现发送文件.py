
SIZE = 5
board = [[0] * SIZE for _ in range(SIZE)]
print(board)
def print_board(board):
    for row in board:
        print(row)
        for col in row:

            print(str(col).center(4), end='')
        print()

print_board(board)