
"""Tic Tac Toe
2-player game in terminal
Detect win conditions properly"""


# I might add validation in future

Grid = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]

Available = 9

# used for converting an integer to a position on grid
def GridRules(x):
    slot = []
    match int(x):
        case 1:
            slot = [0,0]
        case 2:
            slot = [0,1]
        case 3:
            slot = [0,2]
        case 4:
            slot = [1,0]
        case 5:
            slot = [1,1]
        case 6:
            slot = [1,2]
        case 7:
            slot = [2,0]
        case 8:
            slot = [2,1]
        case 9:
            slot = [2,2]
    return slot


def CheckWin(current_grid): 

    player1_win = False
    player2_win = False

    # rows
    for s in current_grid:
        for i in range(0,1):
            if s[i] == s[i+1] and s[i+1] == s[i+2]:
                if s[i] == "*":
                    player1_win = True
                elif s[i] == "/":
                    player2_win = True

    # columns
    for i in range(0,3):
        if current_grid[0][i] == current_grid[1][i] and current_grid[1][i] == current_grid[2][i]:
            if current_grid[0][i] == "*":
                player1_win = True
            elif current_grid[0][i] == "/":
                player2_win = True

    # diagonal
    if current_grid[0][0] == current_grid[1][1] and current_grid[1][1] == current_grid[2][2]:
        if current_grid[0][0] == "*":
            player1_win = True
        elif current_grid[0][0] == "/":
            player2_win = True

    elif current_grid[0][2] == current_grid[1][1] and current_grid[1][1] == current_grid[2][0]:
        if current_grid[0][2] == "*":
            player1_win = True
        elif current_grid[0][2] == "/":
            player2_win = True

    if player1_win:
        return 1
    elif player2_win:
        return 2
    else:
        return 0


while Available > 0:

    player1_inp = input("Player 1: Enter your number 1-9: ")
    pos = GridRules(player1_inp)
    Grid[pos[0]][pos[1]] = "*"
    Available -= 1

    print(*Grid, sep="\n")

    if CheckWin(Grid) == 1:
        print("Player 1 wins!")
        break

    player2_inp = input("Player 2: Enter your number 1-9: ")
    pos2 = GridRules(player2_inp)
    Grid[pos2[0]][pos2[1]] = "/"
    Available -= 1

    print(*Grid, sep="\n")

    if CheckWin(Grid) == 2:
        print("Player 2 wins!")
        break
    