import numpy as np
from player import Guadalupe, Elora
import time

class UltimateBoard(object):
    """docstring for UltimateBoard"""
    def __init__(self):
        self.state = np.empty( (3,3), dtype=object)
        w, h = self.shape
        for x in xrange(w):
            for y in xrange(h):
                self.state[x, y] = Board()
        self.active_board = "any"
    
    def print_state(self):
        w, h = self.shape

        #check if someone win to show it in the print state?
        for x in xrange(w):
            all_lines = [self.state[x, y].print_list() for y in xrange(h)]
            for i in xrange(len(all_lines[0])):
                row = [l[i] for l in all_lines]
                print " " + "  \"  ".join(row) + " "
            if x < w-1:
                print "              \"               \"             "
                print "============================================="
                print "              \"               \"             "
        
    def update(self, move, turn):
        x, y, i, j = move
        self.active_board = self.state[x, y]
        self.active_board.update((i, j), turn)
        next_board = self.state[i, j]
        if next_board.closed:
            self.active_board = "any"
        else:
            self.active_board = next_board 
            #need last board to check winner

    def has_winner(self, move):
        x, y, i, j = move

        if self.state[0, y].closed == self.state[1, y].closed == self.state[2, y].closed in ("x", "o"):
            return True

        if self.state[x, 0].closed == self.state[x, 1].closed == self.state[x, 2].closed in ("x", "o"):
            return True

        if x == y and self.state[0, 0].closed == self.state[1, 1].closed == self.state[2, 2].closed in ("x", "o"):
            return True

        if x + y == 2 and self.state[0, 2].closed == self.state[1, 1].closed == self.state[2, 0].closed in ("x", "o"):
            return True

        return False

    def is_full(self):
        w, h = self.shape
        for x in xrange(w):
            for y in xrange(h):
                if not self.state[x, y].closed:
                    return False
        return True

    @property
    def shape(self):
        return self.state.shape

class Board(object):
    def __init__(self):
        self.state = np.zeros((3,3))
        self.closed = False

    def update(self, move, turn):
        self.state[move[0], move[1]] = 1. - 2 * (turn%2)
        if self.has_winner(move):
            self.closed = ["x", "o"][turn%2]
        if self.is_full():
            self.closed = "draw"

    def has_winner(self, move):
        x, y = move

        if self.state[0, y] == self.state[1, y] == self.state[2, y]:
            return True

        if self.state[x, 0] == self.state[x, 1] == self.state[x, 2]:
            return True

        if x == y and self.state[0, 0] == self.state[1, 1] == self.state[2, 2]:
            return True

        if x + y == 2 and self.state[0, 2] == self.state[1, 1] == self.state[2, 0]:
            return True

        return False

    def is_full(self):
        w, h = self.shape
        return not bool(len([1 for x in xrange(w) for y in xrange(h) if self.state[x, y] == 0]))

    def print_list(self):
        lines = []
        w, h = self.shape
        if self.closed == "x":
            lines = [r"  \     /  ",
                     r"   \   /   ",
                     r"    > <    ",
                     r"   /   \   ",
                     r"  /     \  "]
        elif self.closed == "o":
            lines = [r"   _____   ",
                     r"  /     \  ",
                     r"  |     |  ",
                     r"  \     /  ",
                     r"   -----   "]
        elif self.closed == "draw":
            for x in xrange(w):
                lines.append(" " + " | ".join(["d" for y in xrange(h)]) + " ")
                if x < w-1:
                    lines.append("-----------")
        else:
            for x in xrange(w):
                lines.append(" " + " | ".join([[" ", "x", "o"][int(self.state[x, y])] for y in xrange(h)]) + " ")
                if x < w-1:
                    lines.append("-----------")
        return lines

    def print_state(self):
        for line in self.print_list():
            print line

    @property
    def shape(self):
        return self.state.shape



class Game(object):
    """docstring for Game"""
    def __init__(self, board, player1, player2):
        self.u_board = board
        self.player1 = player1
        self.player2 = player2
        self.turn = 0

    def next_move(self):
        if self.turn%2 == 0:
            next_move = self.player1.move(self.u_board, self.turn)
        elif self.turn%2 == 1:
            next_move = self.player2.move(self.u_board, self.turn)
        self.u_board.update(next_move, self.turn)
        self.turn += 1
        return next_move

    def active_player(self):
        return [self.player1, self.player2][self.turn%2].name
        

if __name__ == '__main__':
    
    ultimate_board = UltimateBoard()
    ultimate_board.print_state()
    game = Game(ultimate_board, Elora(),  Guadalupe())# Guadalupe())
    while True:
        active_player = game.active_player()
        print "turn {} - {} to move".format(game.turn, active_player)
        move = game.next_move()
        print "{} moves to {}. New board state:".format(active_player, move)
        ultimate_board.print_state()
        winner = ultimate_board.has_winner(move)
        
        if winner:
            print active_player + " won"
            break
        elif ultimate_board.is_full():
            print "Draw"
            break
        time.sleep(0.1)