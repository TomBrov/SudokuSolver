from solver import solve
from makeboard import make_board, print_board


def main():
    board = make_board()

    choose = input("would you like to solve yourself: y/n  ")

    if choose.isalpha():
        if choose == "y":
            print_board(board)
            return "Good Luck"
        elif choose == "n":
            solve(board)
            print(board)
            exit(0)
        else:
            return "No choice was selected"
    else:
        return "no choice was selected"


if __name__ == "__main__":
    main()