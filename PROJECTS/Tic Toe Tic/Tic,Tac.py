def sum(a, b, c):
    return a + b + c



def printboard():
    zero = "X" if xStage[0] else ("O" if zStage[0] else 0)
    one = "X" if xStage[1] else ("O" if zStage[1] else 1)
    two = "X" if xStage[2] else ("O" if zStage[2] else 2)
    three = "X" if xStage[3] else ("O" if zStage[3] else 3)
    four = "X" if xStage[4] else ("O" if zStage[4] else 4)
    five = "X" if xStage[5] else ("O" if zStage[5] else 5)
    six = "X" if xStage[6] else ("O" if zStage[6] else 6)
    seven = "X" if xStage[7] else ("O" if zStage[7] else 7)
    eight = "X" if xStage[8] else ("O" if zStage[8] else 8)

    print(f"{zero} | {one} | {two} |")
    print(f"--|---|---|")
    print(f"{three} | {four} | {five} |")
    print(f"--|---|---|")
    print(f"{six} | {seven} | {eight} |")


def check_draw(xStage, zStage):
    # Loop through each cell on the board
    for i in range(9):
        # Check if the cell is occupied by either X or O
        if not (xStage[i] or zStage[i]):
            # If any cell is unoccupied, return False (not a draw)
            return False
    # If all cells are occupied and there is no winner, it's a draw


    return True


def showwin(xStage, zStage):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xStage[win[0]], xStage[win[1]], xStage[win[2]]) == 3:
            print("X Won")
            return 1
        if sum(zStage[win[0]], zStage[win[1]], zStage[win[2]]) == 3:
            print("O Won")
            return 0
    return -1


if __name__ == "__main__":
    xStage = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zStage = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O 
    print('Welcome to Tic Tac Toe')
    while True:
        printboard()
        if turn == 1:
            print("X Choice")
            value = int(input('Enter a value: '))
            xStage[value] = 1
        else:
            print("Z Choice")
            value = int(input('Enter a value: '))
            zStage[value] = 1

        # Check for a draw
        draw=check_draw(xStage,zStage)
        if draw==True:
            print("Match Draw!")
            break

        # Check for a win
        swin = showwin(xStage, zStage)
        if swin != -1:
            print("Match Over")
            break

        turn = 1 - turn
