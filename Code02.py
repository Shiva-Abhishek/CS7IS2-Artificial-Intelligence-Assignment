# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plot

class TicTacToe(object):

    winning_states = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    Suggested_winner = ('X as winner', 'Draw', 'O as winner')

    def __init__(self, squares=[]):
        self.nodes_minimax=0
        self.nodes_alphabeta = 0
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares

    def printboard(self):
        print("")
        print("board:")
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print(element)
        print("")

    def available_moves(self):
        """the spots that are left empty"""
        return [k for k, v in enumerate(self.squares) if v is None]

    def complete(self):
        """to know if the game is over"""
        if None not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False

    def X_winner(self):
        return self.winner() == 'X'

    def O_winner(self):
        return self.winner() == 'O'

    def tied(self):
        return self.complete() == True and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for state in self.winning_states:
                win = True
                for pos in state:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """squares that belong to a player"""
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        """place on square on the board"""
        self.squares[position] = player

    def minimax(self, node, player):
        if node.complete():
            global nodes_minimax
            if node.X_winner():
                self.nodes_minimax += 1
                nodes_minimax = self.nodes_minimax
                return -1
            elif node.tied():
                self.nodes_minimax += 1
                nodes_minimax = self.nodes_minimax
                return 0
            elif node.O_winner():
                self.nodes_minimax += 1
                nodes_minimax = self.nodes_minimax
                return 1
        best = 0
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.minimax(node, get_opponent(player))
            node.make_move(move, None)
            if player == 'O':
                if val > best:
                    best = val
            else:
                if val < best:
                    best = val
        return best

    def alphabeta(self, node, player, alpha, beta):
        if node.complete():
            global nodes_alphabeta
            if node.X_winner():
                self.nodes_alphabeta += 1
                nodes_alphabeta = self.nodes_alphabeta
                return -1
            elif node.tied():
                self.nodes_alphabeta += 1
                nodes_alphabeta = self.nodes_alphabeta
                return 0
            elif node.O_winner():
                self.nodes_alphabeta += 1
                nodes_alphabeta = self.nodes_alphabeta
                return 1
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, get_opponent(player), alpha, beta)
            node.make_move(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha

        if player == 'O':
            return alpha
        else:
            return beta

def computer_move_alphabeta(board, player):
    choices = []
    INF = 9999999999
    a = -INF
    if len(board.available_moves()) == 9:
        return 4
    print("Suggestion for next moves to win:")
    for move in board.available_moves():
        board.make_move(move, player)
        # selecting the best move using alpha beta pruning
        val = board.alphabeta(board, get_opponent(player), -(INF), INF)
        board.make_move(move, None)
        print( "move:", move + 1, "causes:", board.Suggested_winner[val + 1])
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)

    return random.choice(choices)

def computer_move_minimax(board, player):
    choices = []
    INF = 9999999999
    a = -INF
    if len(board.available_moves()) == 9:
        return 4
    print("Suggestion for next moves to win:")
    for move in board.available_moves():
        board.make_move(move, player)
        #selecting the best move using minimax
        val = board.minimax(board, get_opponent(player))
        board.make_move(move, None)
        print( "move:", move + 1, "causes:", board.Suggested_winner[val + 1])
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)

    return random.choice(choices)

def get_opponent(player):
    if player == 'X':
        return 'O'
    return 'X'

def drawGraph():
    print("")
    print("Number of nodes expanded for minimax",nodes_minimax)
    print("Number of nodes expanded for alpha beta pruning",nodes_alphabeta)

    left = ['Minimax', 'Alpha Beta Pruning']
    height = [nodes_minimax, nodes_alphabeta]

    # x axis values
    x = left
    # corresponding y axis values
    y = height

    # plotting the points
    plot.bar(x, y, align='center')

    # naming the x axis
    plot.xlabel('Algorithms')
    # naming the y axis
    plot.ylabel('Nodes Expanded')

    # giving a title to my graph
    plot.title('Comparison of Nodes expanded for algorithms')

    # function to show the plot
    plot.show()

    return

if __name__ == "__main__":
    print("Game playing for minimax")
    board = TicTacToe()
    board.printboard()
    while not board.complete():
        #currently hardcoded as 'X' for human and 'O' for computer
        human_player = 'X'
        print("")
        player_move = int(input("Enter your Next Move: ")) - 1
        if not player_move in board.available_moves():
            continue

        board.make_move(player_move, human_player)
        board.printboard()

        if board.complete():
            break
        human_player = get_opponent(human_player)
        comp_move = computer_move_minimax(board, human_player)
        board.make_move(comp_move, human_player)
        board.printboard()
    print ("Game winner is", board.winner())

    print ("")

    print("Game playing for alpha beta pruning")
    board1 = TicTacToe()
    board1.printboard()
    while not board1.complete():
        # currently hardcoded as 'X' for human and 'O' for computer
        human_player = 'X'
        print("")
        player_move = int(input("Enter your Next Move: ")) - 1
        if not player_move in board1.available_moves():
            continue

        board1.make_move(player_move, human_player)
        board1.printboard()

        if board1.complete():
            break
        human_player = get_opponent(human_player)
        comp_move = computer_move_alphabeta(board1, human_player)
        board1.make_move(comp_move, human_player)
        board1.printboard()
    print("Game winner is", board1.winner())
    drawGraph()


