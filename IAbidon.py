from . import FonctionEvaluation
from . import Board


class Player:

    def __init__(self):
        self.name = "Ninefails"
        # random.seed()
        # self.pos_to_play = [random.randint(0,10), random.randint(0,10)]
        self.board = Board.Board()

    def play(self, board, joueur):
        self.board.get_plateau(board)
        to_play = self.minmax(3, self.board, joueur)
        return to_play

    # def random(self, board):
    #     while board[self.pos_to_play[0]][self.pos_to_play[1]] != 0:
    #         self.pos_to_play = [random.randint(0,10), random.randint(0,10)]
    #     return self.pos_to_play

    def minmax(self, depth, board, joueur):
        max_val = -200

        for coup in board.legal_plays(board.plateau):
            x, y = coup
            board.next_state((x, y), joueur)
            print("OKKKKKKKKKKK")

            val = self.min(depth, coup, board, joueur)
            print("OKKKKKKKKKKK")

            if val > max_val:
                max_val = val
                meilleurCoup = coup
            board.reset_nextplateau()

        return meilleurCoup

    def min(self, depth, coup, board, joueur):
        x, y = coup

        if depth == 0:
            return FonctionEvaluation.fonctionEvaluation(x, y, board.nextplateau, -joueur)

        min_val = 200

        for nextCoup in board.legal_plays(board.nextplateau):
            nx, ny = nextCoup
            board.next_state((nx, ny), -joueur)

            val = self.max(depth-1, nextCoup, board, joueur)

            if val < min_val:
                min_val = val
            board.reset_nextplateau()

        return min_val

    def max(self, depth, coup, board, joueur):
        x, y = coup
        if depth == 0:
            return FonctionEvaluation.fonctionEvaluation(x, y, board.nextplateau, joueur)

        max_val = -200

        for nextCoup in board.legal_plays(board.nextplateau):
            nx, ny = nextCoup
            board.next_state((nx, ny), joueur)
            val = self.min(depth - 1, nextCoup, board, joueur)

            if val > max_val:
                max_val = val
            board.reset_nextplateau()

        return max_val

    def laFlemme(self, board, joueur):
        valeurMax = -200
        meilleurCoup = (0, 0)
        for coup in board.legal_plays(board.plateau):
            x, y = coup
            valeur = FonctionEvaluation.fonctionEvaluation(x, y, board.plateau, joueur)
            if valeur > valeurMax:
                valeurMax = valeur
                meilleurCoup = coup

        return coup
