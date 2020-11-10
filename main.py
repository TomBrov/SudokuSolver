from solver import solve, valid, print_board
from boards import board_1, board_2, board_3

boards = {"easy": board_1, "medium": board_2, "hard": board_3}
b = input("Please choose your level\n"
          "Easy, Medium, Hard: ")
bo = boards[b]

if b.isalpha():
    solve(bo)
    print_board(bo)
else:
    print("No Level was chosen. Exiting.")
