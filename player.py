import random 

class Guadalupe(object):
    """docstring for Player"""
    def __init__(self):
        self.name = "Guadalupe"

    def move(self, board, turn):
        w, h = board.shape
        move_set = [(x, y) for x in xrange(w) for y in xrange(h) if board.state[x, y] == 0 ]
        print move_set

        move = random.sample(move_set, 1)[0]
        return move


class Elora(object):
    """docstring for Player"""
    def __init__(self):
        self.name = "Elora"

    def move(self, board, turn):
        w, h = board.shape
        move_set = [(x, y) for x in xrange(w) for y in xrange(h) if board.state[x, y] == 0 ]
        print move_set

        move = random.sample(move_set, 1)[0]
        return move



        