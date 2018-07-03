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
        import brain
        self.brain = brain.Brain([9, 6, 9])

    def move(self, board, turn):
        w, h = board.shape
        
        inputs = board.state.reshape(1,9).tolist()[0]
        results = self.brain.propagate(inputs, 0)
        all_moves = [(x, y) for x in xrange(w) for y in xrange(h)]
        legal_moves = [(x, y) for x in xrange(w) for y in xrange(h) if board.state[x, y] == 0]
        for i, r in enumerate(sorted(results, reverse = True)):
            print r
            if all_moves[i] in legal_moves:
                return all_moves[i]
        else:
            print "no legal moves"
            return False






        