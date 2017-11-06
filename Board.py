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

    def get_plateau(self, bo):
        # Returns a representation of the starting state of the game.
        self.plateau = bo

    def reset_nextplateau(self):
        self.nextplateau = self.plateau

    def next_state(self, pos, joueur):
        # Takes the game state, and the move to be applied.
        # Returns the new game state.
        posx, posy = pos
        self.nextplateau[posx][posy] = joueur
        pass

    def legal_plays(self, plateau):
        # Takes a sequence of game states representing the full
        # game history, and returns the full list of moves that
        # are legal plays for the current player.

        # self.get_plateau()

        legalMoves = []
        for i in range(11):
            for j in range(11):
                if plateau[i][j] == 0:
                    legalMoves.append([i, j])
        return legalMoves
        pass
