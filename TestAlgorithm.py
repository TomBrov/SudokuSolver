import getpass, random

username = getpass.getuser()
screen = {k + 1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0} for k in range(9)}


def invoke_random_suduko():
    try_again = "Empty"
    wrong = "Wrong choice! \nDo you want to try again? \nType Yes if you want: "
    while try_again == "Empty" or try_again == "Yes":
        diff = input("Choose suduko difficulty, from 1 (Easy) to 5 (Tough): ")
        if diff.isdigit():
            if int(diff) == 1:
                for value in range(1, 31):
                    screen[random.randrange(1, 9)][random.randrange(1, 9)] = (random.randrange(1, 9))
                    value = value + 1
                try_again = "No"
            elif int(diff) == 2:
                for value in range(1, 25):
                    screen[random.randrange(1, 9)][random.randrange(1, 9)] = (random.randrange(1, 9))
                    value = value + 1
                    try_again = "No"
            elif int(diff) == 3:
                for value in range(1, 19):
                    screen[random.randrange(1, 9)][random.randrange(1, 9)] = (random.randrange(1, 9))
                    value = value + 1
                    try_again = "No"
            elif int(diff) == 4:
                for value in range(1, 13):
                    screen[random.randrange(1, 9)][random.randrange(1, 9)] = (random.randrange(1, 9))
                    value = value + 1
                    try_again = "No"
            elif int(diff) == 5:
                for value in range(1, 7):
                    screen[random.randrange(1, 9)][random.randrange(1, 9)] = (random.randrange(1, 9))
                    value = value + 1
                    try_again = "No"
            else:
                try_again = input(wrong)
        else:
            try_again = input(wrong)


def find_empty_cells():
    empty_cells = {}
    for block in range(1, 10):
        for square in range(1, 10):
            if screen[block][square] == 0:
                empty_cells.update({block: square})
                square = square + 1
        block = block + 1
    return empty_cells


invoke_random_suduko()
print(find_empty_cells())

