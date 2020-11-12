from solver import solve, print_board
from makeboard import make_board


def main():
    new = make_board()

    board = input("would you like to solve yourself: y/n  ")

    if board.isalpha():
        if board == "y":
            return "Good Luck"
        elif board == "n":
            solve(new)
            print(new)
            exit(0)
        else:
            return "No choice was selected"
    else:
        return "no choice was selected"

if __name__ == "__main__":
    main()