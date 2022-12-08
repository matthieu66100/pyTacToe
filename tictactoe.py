# Init grid
grid = [
[' 1 ',' | ',' 2 ',' | ',' 3 '],
['---',' | ','---',' | ','---'],
[' 4 ',' | ',' 5 ',' | ',' 6 '],
['---',' | ','---',' | ','---'],
[' 7 ',' | ',' 8 ',' | ',' 9 ']
]

###############################
#   Print visual board game   #
###############################
def printGrid():
    for r in grid:
        print("")
        for c in r:
            print(c, end="")
    print('\n')

###############################
#  change values in the board #
###############################
def modifyTable(nb, mark):
    if(nb == 1):
        grid[0][0] = mark
    if(nb == 2):
        grid[0][2] = mark
    if(nb == 3):
        grid[0][4] = mark
    if(nb == 4):
        grid[2][0] = mark
    if(nb == 5):
        grid[2][2] = mark
    if(nb == 6):
        grid[2][4] = mark
    if(nb == 7):
        grid[4][0] = mark
    if(nb == 8):
        grid[4][2] = mark
    if(nb == 9):
        grid[4][4] = mark


###############################
#       Verify win event      #
###############################
def winCheck(grid):
    #check the horizontals win
    if grid[0][0] == grid[0][2] == grid[0][4]:
        return True
    if grid[2][0] == grid[2][2] == grid[2][4]:
        return True
    if grid[4][0] == grid[4][2] == grid[4][4]:
        return True

    #check the verticals win
    if grid[0][0] == grid[2][0] == grid[4][0]:
        return True
    if grid[0][2] == grid[2][2] == grid[4][2]:
        return True
    if grid[0][4] == grid[2][4] == grid[4][4]:
        return True

    #check the diagonals win
    if grid[0][0] == grid[2][2] == grid[4][4]:
        return True
    if grid[4][0] == grid[2][2] == grid[0][4]:
        return True
    
    else: return False
    

###############################
#             Game            #
###############################

def game():
    markSelect = ' O ',' X '
    isPlayer = 0

    printGrid()

    while True:
        #select cross or round
        if(isPlayer % 2) == 0:
            mark = markSelect[1]
        else:
            mark = markSelect[0]

        # force the input to take integer value
        nb = int(input('select number:'))

        modifyTable(nb, mark)
        printGrid()

        isPlayer = isPlayer + 1

        # check if one player win the game and break the game
        if winCheck(grid):
            print('Player: (' + mark + ') You Win!')
            input('Press "Enter" on your keyboard to quit')
            break
    


game()