import getpass, random

username = getpass.getuser()
screen = {k + 1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0} for k in range(9)}


def Make_Board():
    Grid = [[0 for x in range(9)] for y in range(9)]
            
    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0
            
    # The range here is the amount
	# of numbers in the grid
    
    diffdict = {1 : 35, 2 : 30, 3 : 25, 4 : 17, 5 : 10}  
    diff = input("Choose suduko difficulty, from 1 (Easy) to 5 (Tough): ")
    diff = int(diff)
    d = diffdict[diff]
    
    for i in range(d):
        #choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while(not CheckValid(Grid,row,col,num) or Grid[row][col] != 0): #if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        Grid[row][col]= num;
        
    Printgrid(Grid)


def Printgrid(Grid):
    for i in range(len(Grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(Grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(Grid[i][j])
            else:
                print(str(Grid[i][j]) + " ", end="")
                
    
def CheckValid(Grid,row,col,num):
    #check if in row
    valid = True
    #check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            #check if section is valid
            if(Grid[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid


if __name__ == "__main__":
    Make_Board()

