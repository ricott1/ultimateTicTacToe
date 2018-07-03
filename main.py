import numpy as np
from player import Guadalupe, Elora
import time

class Board(object):
    def __init__(self):
        self.state = np.zeros((3,3))

    def update(self, move, turn):
        self.state[move[0], move[1]] = 1. - 2 * (turn%2)

    def has_winner(self, move):
        x, y = move

        if self.state[0][y] == self.state[1][y] == self.state[2][y]:
            return True

        if self.state[x][0] == self.state[x][1] == self.state[x][2]:
            return True

        if x == y and self.state[0][0] == self.state[1][1] == self.state[2][2]:
            return True

        if x + y == 2 and self.state[0][2] == self.state[1][1] == self.state[2][0]:
            return True

        return False

    def is_full(self):
        w, h = self.shape
        return not bool(len([1 for x in xrange(w) for y in xrange(h) if self.state[x, y] == 0]))

    def print_state(self):
        w, h = self.shape
        for x in xrange(w):
            print " " + " | ".join([[" ", "o", "x"][int(self.state[x, y])] for y in xrange(h)]) + " "
            if x < w-1:
                print "-----------"

    @property
    def shape(self):
        return self.state.shape



class Game(object):
    """docstring for Game"""
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.turn = 0

    def next_move(self):
        if self.turn%2 == 0:
            next_move = self.player1.move(self.board, self.turn)
        elif self.turn%2 == 1:
            next_move = self.player2.move(self.board, self.turn)
        self.board.update(next_move, self.turn)
        self.turn += 1
        return next_move

    def active_player(self):
        return [self.player1, self.player2][self.turn%2].name
        

if __name__ == '__main__':
    board = Board()
    game = Game(board, Elora(), Guadalupe())

    while True:
        active_player = game.active_player()
        print "turn {} - {} to move".format(game.turn, active_player)
        move = game.next_move()
        print "{} moves to {}. New board state:".format(active_player, move)
        board.print_state()
        winner = board.has_winner(move)
        if board.is_full():
            print "Draw"
            break
        elif winner:
            print active_player + " won"
            break
        time.sleep(1)