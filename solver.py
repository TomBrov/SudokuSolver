import numpy as np
from boards import *

'''
Not Done
Not Done
Not Done
Not Done
Not Done
'''


def solve(board):
    board = np.array(board)

    solved = False
    while not solved:
        zeros = np.where(board == 0)
        if len(zeros[0]) == 0:
            solved = True
            continue
        zeros = set(zip(zeros[0], zeros[1]))

        for zero in zeros:
            for num in range(1, 10):
                if checkRC(board, zero, num):
                    board[zero[0]][zero[1]] = num
                else:
                    continue

    print_board(board)

def checkRC(board, pos, num):
    for i in range(0, 9):
        #Check row/col
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

solve(board_1)
