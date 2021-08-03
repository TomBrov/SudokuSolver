from solver import solve, print_board
from boards import *


def main():
    boards = {'1': board_1, '2': board_2, '3': board_3}

    user = input("What is your name: ")

    diff = input(f"Hello {user}\n"
                 "3 Boards are available\n"
                 "Board 1, 2 or 3\n"
                 "Please choose a board to solve (No. Only): ")
    board = boards[diff]
    print_board(board)

    choice = input("Would you like to solve it yourself?\n"
                   "Please type yes or no:  ")

    if choice == 'yes':
        print("good luck")
        exit(0)
    elif choice == 'no':
        solve(board)
        print_board(board)
    else:
        print("Invalid choice. Exiting...")
        exit(0)


if __name__ == "__main__":
    main()