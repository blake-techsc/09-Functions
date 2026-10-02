usedList = []
gameEnded = False
playerX = True

def printBoard(board):
    """Prints out the board with a lenght and height of 3"""
    print("  ", end="")
    for i in range(len(board[0])):
        print(i, end=" ")
    print()
    for i in range(len(board)):
        print(i, end=" ")
        for r in board[i]:
            print(r, end=" ")
        print()
    print("")

def get_valid_int(usedList):
    """Checks to see if the user input is valid, must be between 0-2"""
    while True:
        try:
            column = int(input("Enter a column: "))
            row = int(input("Enter a row: "))
            if 0 <= column <= 2 and 0 <= row <= 2:
                if [row, column] in usedList:
                    print("Spot is taken, try again")
                    continue
                else:
                    usedList.append([row, column])
                    return row, column
            else:
                print("Value must be between 0-2, try again")
        except ValueError:
            print("Invalid, try again")

def modifyBoard(board, row, column, player_x, usedList=None):
    """Changes the board from the user's turns"""
    symbol = "X" if player_x else "O"
    board[row][column] = symbol
    return board

def checkWin(board):
    """Checks to see if there's any matches of three diagonally, horizontally, and vertically"""
    for r in range(len(board)):
        if board[r][0] == board[r][1] == board[r][2] and board[r][0] != "-":
            print(f"Player {board[r][0]} wins!")
            return True

    for c in range(len(board[0])):
        if board[0][c] == board[1][c] == board[2][c] and board[0][c] != "-":
            print(f"Player {board[0][c]} wins!")
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        print(f"Player {board[0][0]} wins!")
        return True
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        print(f"Player {board[0][2]} wins!")
        return True
    return False

def checkTie(board):
    """Checks to see if there's no spaces left"""
    for row in board:
        if "-" in row:
            return False
    print("It's a tie!")
    return True

def playAgain():
    """Asks if """
    while True:
        response = input("Play again? (Y/N): ").strip().upper()
        if response == "Y":
            return True
        elif response == "N":
            return False
        else:
            print("Enter Y or N.")

def initializeBoard(size=3):
    """Prints out the board"""
    return [["-" for _ in range(size)] for _ in range(size)]

while True:
    board = initializeBoard()
    printBoard(board)
    while not gameEnded:
        playerSymbol = "X" if playerX else "O"
        print(f"Player {playerSymbol}'s turn")
        row, column = get_valid_int(usedList)
        modifyBoard(board, row, column, playerX, usedList)
        printBoard(board)
        if checkWin(board):
            gameEnded = True
        elif checkTie(board):
            gameEnded = True
        else:
            playerX = not playerX
    if not playAgain():
        print("Bye bye")
        break
