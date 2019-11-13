#! python3

# Tic Tac Toe

import random, copy, sys

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def mainMenu():
    # This is the main menu where the player can decide if they want to play solo or with someone else

    playing = True

    while playing:
        print('1 Player or 2 Players?')
        numPlayer = input()
        if numPlayer == '1':
            onePlayer()
        elif numPlayer == '2':
            twoPlayer()
        else:
            mainMenu()
    

def drawBoard(board):
    # This function prints out the board that it was passed

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def inputPlayerLetter():
    # Let's the player type which letter they want to be
    # Returns a list with the players letters as the first item, and the computer's letters as the second
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # The first element in the tuple is the player's letter, the second is the computer's letter
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first
    if random.randint(0, 1) ==0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False
    # on a False read the game will quit
    restart = True
    
    while restart:
        print('Press enter to restart or q to quit!')
        restart = input()
        if restart == "q":
            restart = False
            sys.exit()

    mainMenu()

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this funciton returns True if the player has won
    # We use bo instead of board and le instead of letter so we don't have to type as much
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or # across the top
            (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or # across the middle
            (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or # across the bottom
            (bo['low-L'] == le and bo['mid-L'] == le and bo['top-L'] == le) or # down the left side
            (bo['low-M'] == le and bo['mid-M'] == le and bo['top-M'] == le) or # down the middle
            (bo['low-R'] == le and bo['mid-R'] == le and bo['top-R'] == le) or # down the right side
            (bo['low-L'] == le and bo['mid-M'] == le and bo['top-R'] == le) or # diagonal
            (bo['low-R'] == le and bo['mid-M'] == le and bo['top-L'] == le)) # diagonal

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move
    move = ' '
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move):
        print('What is your next move? (top-, mid-, low- & L, M, R)')
        move = input()
    return move

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board
    # Returns None if there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i

    # Try to take one of the corners if they are free
    move = chooseRandomMoveFromList(board, ['top-L', 'top-R', 'low-L', 'low-R'])
    if move != None:
        return move

    # Try to take the center if it is free
    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'

    # Move on one of the sides
    return chooseRandomMoveFromList(board, ['top-M', 'low-M', 'mid-L', 'mid-R'])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        if isSpaceFree(board, i):
            return False
    return True

def onePlayer():
    print('Welcome to Tic Tac Toe!')
    
    while True:
        # Reset the board
        theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first')

        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                # Computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
                    
        if not playAgain():
            break

def playerOder():
    # Randomly choose the player who goes first
    if random.randint(0, 1) ==0:
        return 'player 1'
    else:
        return 'player 2'

def getPlayer2Move(board):
    # Let the player type in his move
    move = ' '
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move):
        print('What is your next move? (top-, mid-, low- & L, M, R)')
        move = input()
    return move

def twoPlayer():
     print('Welcome to Tic Tac Toe!')

     while True:
         # Reset the board
         theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                     'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                     'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

         playerLetter, player2Letter = inputPlayerLetter()
         turn = whoGoesFirst()
         print('The ' + turn + ' will go first')

         gameIsPlaying = True

         while gameIsPlaying:


             # Player 1 takes their turn
             if turn == 'player 1':
                 drawBoard(theBoard)
                 move = getPlayerMove(theBoard)
                 makeMove(theBoard, playerLetter, move)
    
                 if isWinner(theBoard, playerLetter):
                     drawBoard(theBoard)
                     print('Hooray! You have won the game!')
                     gameIsPlaying = False
                 else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        gameIsPlaying = False
                    else:
                        turn = 'player 2'
                        

             # Player 2 takes their turn
             else:
                 drawBoard(theBoard)
                 move = getPlayer2Move(theBoard)
                 makeMove(theBoard, player2Letter, move)

                 if isWinner(theBoard, player2Letter):
                     drawBoard(theBoard)
                     print('Hooray! You have won the game!')
                     gameIsPlaying = False
                 else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player 1'

         if not playAgain():
             break
                        

# Open the main menu
mainMenu()
