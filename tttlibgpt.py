BOARD_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
WINNERS = [('1', '2', '3'),
           ('4', '5', '6'),
           ('7', '8', '9'),
           ('1', '4', '7'),
           ('2', '5', '8'),
           ('3', '6', '9'),
           ('1', '5', '9'),
           ('3', '5', '7')]

def displayBoard(xSpaces: set, oSpaces: set):
    '''clear screen and re-display board, display x and o 
    instead of numbers for the ones chosen'''
    print("\033[H\033[2J", end="")  # clear screen
    board = []
    for space in BOARD_SPACES:
        if space in xSpaces:
            board.append("x")
        elif space in oSpaces:
            board.append("o")
        else:
            board.append(space)

    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print("---+---+---")
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print("---+---+---")
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def isWinner(spaces: set) -> bool:
    '''returns true if any of the combinations are in the 
    winners list'''
    for combination in WINNERS:
        if spaces.issuperset(combination):
            return True


def getValidMoves(takenSpaces: set) -> set:
    '''returns a set of spaces that are not in taken spaces'''
    return set(BOARD_SPACES) - takenSpaces


def humanMove(mySpaces: set, opponentSpaces: set) -> set:
    """get a valid tic-tac-toe move from human"""
    chosenMove = input("choose a valid move")
    while chosenMove not in getValidMoves(mySpaces | opponentSpaces):
        chosenMove = input("choose a valid move")
    return {chosenMove}


def playGame(playerXmove: callable, playerOmove: callable) -> str:
    """play a game of tic-tac-toe.
    arguments:
      playerXmove
        function with signature
          f(mySpaces:set opponentSpaces:set) -> str
            must return a valid move to be played for X
      playerOmove
        function with signature
          f(mySpaces:set, opponentSpaces:set) -> str
            must return a valid move to be played for """
    xSpaces = set()
    oSpaces = set()
    while True:
        # get player X move
        displayBoard(xSpaces, oSpaces)
        print("It is X's turn")
        xChooses = playerXmove(xSpaces, oSpaces)
        xSpaces.update(xChooses)
        # to see if x won
        if isWinner(xSpaces):
            displayBoard(xSpaces, oSpaces)
            print("X wins")
            return "X"
        # checking for draw
        if len(xSpaces) + len(oSpaces) == 9:
            displayBoard(xSpaces, oSpaces)
            print("It's a draw")
            return
        # get player O move
        displayBoard(xSpaces, oSpaces)
        print("It is O's turn")
        oChooses = playerOmove(xSpaces, oSpaces)
        oSpaces.update(oChooses)
        # to see if O won
        if isWinner(oSpaces):
            displayBoard(xSpaces, oSpaces)
            print("O wins")
            return "O"
        # checking for draw
        if len(xSpaces) + len(oSpaces) == 9:
            displayBoard(xSpaces, oSpaces)
            print("It's a draw")
            return

if __name__ == '__main__':
    playGame(humanMove, humanMove)