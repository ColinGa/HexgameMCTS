from hexgame import *


class Board(object):
    def __init__(self):
        self.plateau = []
        self.nextplateau = []
        for i in range(11):
            self.plateau.append([0]*11)
            self.nextplateau.append([0] * 11)
        self.legalMoves = []
        pass

    def get_plateau(self):
        # Returns a representation of the starting state of the game.
        self.plateau = Game.board
        pass

    def next_state(self, pos):
        # Takes the game state, and the move to be applied.
        # Returns the new game state.
        posx, posy = pos
        self.nextplateau = self.plateau
        self.nextplateau[posx][posy] = 1
        pass

    def legal_plays(self):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.
        self.get_plateau()

        for i, j in range(0, 10):
            if self.plateau[i][j] == 0:
                self.legalMoves.append([i, j])
        return self.legalMoves
        pass
