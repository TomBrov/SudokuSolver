import getpass
import random
from solver import print_board

username = getpass.getuser()
screen = {k + 1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0} for k in range(9)}


def make_board():
    board = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            board[i][j] = 0

    # The range here is the amount
    # of numbers in the grid

    diff_dict = {1: 35, 2: 30, 3: 25, 4: 17, 5: 10}
    diff = input("Choose Sudoku difficulty, from 1 (Easy) to 5 (Tough): ")
    diff = int(diff)
    d = diff_dict[diff]

    for i in range(d):
        # choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while not valid(board, row, col, num) or board[row][col] != 0:
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        board[row][col] = num

    return board


def valid(board, row, col, num):
    # check if in row
    valid = True
    # check row and collumn
    for x in range(9):
        if board[x][col] == num:
            valid = False
    for y in range(9):
        if board[row][y] == num:
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is valid
            if board[rowsection * 3 + x][colsection * 3 + y] == num:
                valid = False
    return valid


if __name__ == "__main__":
    make_board()
