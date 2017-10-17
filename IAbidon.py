import random

class Player:

    def __init__(self):
        random.seed()

    def play(self, board, joueur):
        to_play = heuristique(board)
        return to_play

    def random(self, board):
        while board[pos_to_play[0]][pos_to_play[1]] != 0:
            pos_to_play = [random.randint(0,10), random.randint(0,10)]
        return pos_to_play
    


#JEU TEST
#Declaration du plateau
# board = [] #Cette liste contiendra ma map en 2D
# for i in range(11):
#     board.append([0] * 11)
# boolean = True
# joueur = 1
# for i in range(121):
#     if boolean:
#         pos = play(board, 1)
#         boolean = False
#         joueur = 1
#     else:
#         pos = play(board, -1)
#         boolean = True
#         joueur = -1
#     board[pos[0]][pos[1]] = joueur
# print(board)