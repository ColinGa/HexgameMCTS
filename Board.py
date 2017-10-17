import numpy as np
from Mcts_hex import *

class Board(object):

    def start(self):
        # Returns a representation of the starting state of the game.
        self.plateau = np.zeros((11, 11), int)
        pass

    def next_state(self, state, play):
        # Takes the game state, and the move to be applied.
        # Returns the new game state.

        pass

    def legal_plays(self, state_history):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.
        pass

    def winner(self, state_history):
        # Takes a sequence of game states representing the full
        # game history.  If the game is now won, return the player
        # number.  If the game is still ongoing, return zero.  If
        # the game is tied, return a different distinct value, e.g. -1.
        pass