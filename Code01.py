# -*- coding: utf-8 -*-

# Total States Counting Variable
totalStates = 0


class Game:
    """
    class Game store a instance of the game
    """
    __slots__ = 'grid'

    def __init__(self):
        self.grid = [' ' for i in range(9)]

    def stateCopy(self, g2):
        self.grid = []
        for c in g2:
            self.grid.append(str(c))

    def markGrid(self, n, isHuman):
        if n > len(self.grid) or n < 1:
            print("invalid move, check position and re enter")
            return False
        if self.grid[n - 1] != ' ':
            print("invalid move, check position and re enter")
            return False
        if isHuman:
            self.grid[n - 1] = 'X'
        else:
            self.grid[n - 1] = 'O'

        return True

    def __str__(self):
        s = ''
        s += (str(self.grid[0]) + ' | ' + str(self.grid[1]) + ' | ' + str(self.grid[2]) + '  ') + '\n'
        s += '----------\n'
        s += (str(self.grid[3]) + ' | ' + str(self.grid[4]) + ' | ' + str(self.grid[5]) + '  ') + '\n'
        s += '----------\n'
        s += (str(self.grid[6]) + ' | ' + str(self.grid[7]) + ' | ' + str(self.grid[8]) + '  ') + '\n'
        return s


def isGameDraw(game):
    for i in range(0, len(game.grid)):
        if game.grid[i] == ' ':
            return False
    return True


def computerWon(t):
    # Left Vertical
    if t.grid[0] != ' ' and t.grid[0] == t.grid[3] and t.grid[3] == t.grid[6]:
        if t.grid[0] == 'O':
            return 1
        elif t.grid[0] == 'X':
            return -1
    # Middle Vertical
    if t.grid[1] != ' ' and t.grid[1] == t.grid[4] and t.grid[4] == t.grid[7]:
        if t.grid[1] == 'O':
            return 1
        elif t.grid[1] == 'X':
            return -1
    # Right Vertical
    if t.grid[2] != ' ' and t.grid[2] == t.grid[5] and t.grid[5] == t.grid[8]:
        if t.grid[2] == 'O':
            return 1
        elif t.grid[2] == 'X':
            return -1
    # Top horizontal
    if t.grid[0] != ' ' and t.grid[0] == t.grid[1] and t.grid[1] == t.grid[2]:
        if t.grid[0] == 'O':
            return 1
        elif t.grid[0] == 'X':
            return -1
    # Horizontal Middle
    if t.grid[3] != ' ' and t.grid[3] == t.grid[4] and t.grid[4] == t.grid[5]:
        if t.grid[3] == 'O':
            return 1
        elif t.grid[3] == 'X':
            return -1
    # Horizontal Bottom
    if t.grid[6] != ' ' and t.grid[6] == t.grid[7] and t.grid[7] == t.grid[8]:
        if t.grid[6] == 'O':
            return 1
        elif t.grid[6] == 'X':
            return -1
    # Diagonal Top left to Bottom Right
    if t.grid[0] != ' ' and t.grid[0] == t.grid[4] and t.grid[4] == t.grid[8]:
        if t.grid[0] == 'O':
            return 1
        elif t.grid[0] == 'X':
            return -1
    # Diagonal Top Right to Bottom Left
    if t.grid[2] != ' ' and t.grid[2] == t.grid[4] and t.grid[4] == t.grid[6]:
        if t.grid[2] == 'O':
            return 1
        elif t.grid[2] == 'X':
            return -1
    return 0


def mini_max(game, isMax):
    """
    get the best move using miniMax algorithm
    :param game: game instance
    :param isMax: boolean stating is it maxPlayer turn
    :return: best result (i.e. how good this path is)
    """
    global totalStates
    maxVal = -100  # represent - infinity for this problem
    minVal = 100  # represent + infinity for this problem
    gamePiece = 'O' if isMax else 'X'

    winner = computerWon(game)
    if winner != 0:
        # totalStates -= 1
        return winner

    elif isGameDraw(game):
        # totalStates -= 1
        return 0

    totalStates += 1


    for move in range(0, 9):

        if game.grid[move] == ' ':

            game.grid[move] = gamePiece
            val = mini_max(game, not isMax)

            game.grid[move] = ' '

            # Max player
            if isMax:
                if val > maxVal:
                    maxVal = val

            # Min Player
            else:
                if val < minVal:
                    minVal = val

    if isMax:
        return maxVal
    else:
        return minVal


def alphaPruning(game, isMax, a, b):
    """
    get the best move using alpha beta pruning
    :param game: game instance
    :param isMax: boolean stating is it maxPlayer turn
    :param a: alpha
    :param b: beta
    :return: best result (i.e. how good this path is)
    """
    global totalStates
    gamePiece = 'O' if isMax else 'X'

    winner = computerWon(game)
    if winner != 0:
        # totalStates -= 1
        return winner

    elif isGameDraw(game):
        # totalStates -= 1
        return 0
    totalStates += 1


    for move in range(0, 9):

        if game.grid[move] == ' ':

            game.grid[move] = gamePiece
            val = alphaPruning(game, not isMax, a, b)

            game.grid[move] = ' '

            # Max player
            if isMax:
                if val > a:
                    a = val

            # Min Player
            else:
                if val < b:
                    b = val
        if a >= b:
            break  # prune

    if isMax:
        return a
    else:
        return b


def computerMove(game, byMinMax):
    """
    Computes the next move for computer
    :param game: game instance
    :param byMinMax: boolean stating we need to calculate using MinMax
    :return: best move
    """
    maxVal = -100  # represents -infinity for this problem
    possibleMove = []
    global totalStates
    totalStates = 0
    for i in range(9):
        if game.grid[i] == ' ':
            game.grid[i] = 'O'
            if byMinMax:
                val = mini_max(game, False)
            else:
                val = alphaPruning(game, False, -100, 100)
            game.grid[i] = ' '
            if val > maxVal:
                maxVal = val
                possibleMove = [i]
            elif val == maxVal:
                possibleMove.append(i)
    return possibleMove[0]


def main():
    """
    main method of the module
    :return:
    """
    humanTurn = True
    totalMove = 0
    t = Game()
    print('************* Tic Tac Toe ****************************************')
    print('Human uses X marker and Computer uses O marker')
    print('User is required to read the message and enter next move')
    print('User input format:')
    print('1  | 2 | 3  ')
    print('-----------')
    print('4  | 5 | 6  ')
    print('-----------')
    print('7  | 8 | 9  ')
    print('******************************************************************\n')
    # t.grid = ['X','X',' ','O','O',' ','X','O',' ']
    while computerWon(t) == 0 and totalMove < 9:
        if humanTurn:
            print(t)
            inp = input('For Above board enter your move as grid# :')
            inp = inp.replace(' ', '')
            if t.markGrid(int(inp), True):
                humanTurn = False
                totalMove += 1
        else:
            print(t)
            miniMaxRes = computerMove(t, True)
            print("Using MiniMax: \n\t\ttotal states explored: " + str(totalStates))
            print("\t\tNext Move: " + str(miniMaxRes))
            alphabetRes = computerMove(t, False)
            print("Using AlphaBeta: \n\t\ttotal states explored: " + str(totalStates))
            print("\t\tNext Move: " + str(alphabetRes))
            if t.markGrid(int(miniMaxRes) + 1, False):
                humanTurn = True
                totalMove += 1
    # t.grid = ['X','X','O','X','O','X','X','O','X']
    print(t)
    res = computerWon(t)
    if res == 1:
        print("COMPUTER WON")
    elif res == -1:
        print("PLAYER WON")
    else:
        print("DRAW")


main()
