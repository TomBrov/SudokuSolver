from solver import solve, print_board
from makeboard import make_board


def main():
    make_board()

    board = input("would you like to solve yourself: y/n  ")

    if board.isalpha():
        if board == "y":
            print_board(grid)
        elif board == "n":
            solve(grid)
            print(grid)
            exit(0)
        else:
            return "No choice was selected"
    else:
        return "no choice was selected"