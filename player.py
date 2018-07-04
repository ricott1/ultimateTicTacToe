import random 
import numpy as np

class Guadalupe(object):
    """Guadalupe plays a random legal move"""
    def __init__(self):
        self.name = "Guadalupe"

    def move(self, board, turn):
        w, h = board.state[0,0].shape
        if board.active_board != "any":
            x, y = np.where(board.state == board.active_board)
            x = x[0]
            y= y[0]
        else:
            x, y = random.sample([(i, j) for i in xrange(w) for j in xrange(h) if not board.state[i, j].closed], 1)[0]
        print x, y
        move_set = [(x, y, i, j) for i in xrange(w) for j in xrange(h) if board.state[x, y].state[i, j] == 0 ]
        
        if move_set:
            return random.sample(move_set, 1)[0]
        else:
            return False


class Elora(object):
    """Elora uses a neural network to generate the best move. She is trained with genetic selection"""
    def __init__(self):
        self.name = "Elora"
        import brain
        self.brain = brain.Brain([81, 6, 9])

    def move(self, board, turn):
        w, h = board.shape
        inputs = []
        for x in xrange(w):
            for y in xrange(h):
                inputs.append(board.state[x, y].state.reshape(1, 9).tolist()[0])
        inputs = [j for i in inputs for j in i]
        if board.active_board != "any":
            x, y = np.where(board.state == board.active_board)
            x = x[0]
            y= y[0]
        else:
            x, y = random.sample([(i, j) for i in xrange(w) for j in xrange(h) if not board.state[i, j].closed], 1)[0]
        
        
        results = self.brain.propagate(inputs, 0)
        all_moves = [(x, y, i, j) for i in xrange(w) for j in xrange(h)]
        legal_moves = [(x, y, i, j) for i in xrange(w) for j in xrange(h) if board.state[x, y].state[i, j] == 0]
        for i, r in enumerate(sorted(results, reverse = True)):
            if all_moves[i] in legal_moves:
                return all_moves[i]
        else:
            print "no legal moves"
            return False






        